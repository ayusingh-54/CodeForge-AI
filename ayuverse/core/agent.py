"""
CodeForge AI Agent - LangChain-based autonomous coding agent
Uses LangGraph for workflow orchestration with enhanced reasoning capabilities
Author: Ayush Singh
"""
from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os

from ayuverse.tools.registry import ToolRegistry, ToolResult
from ayuverse.utils.helpers import _parse_json, _clip
from ayuverse.core.state import AgentState


class CodeForgeAgent:
    """
    Advanced AI agent using LangChain for reasoning and LangGraph for orchestration.
    Implements an enhanced ReAct pattern with better tool selection and error recovery.
    """
    
    def __init__(self, tool_registry: ToolRegistry, agent_state: AgentState, 
                 model: str = "gpt-4o-mini", temperature: float = 0.1):
        self.tool_registry = tool_registry
        self.agent_state = agent_state
        self.messages = []
        
        # Initialize OpenAI chat model via LangChain
        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            api_key=os.environ.get("OPENAI_API_KEY"),
            streaming=False
        )
        
        self.system_prompt = self._build_system_prompt()
    
    def _build_system_prompt(self) -> str:
        """Build comprehensive system prompt for the agent."""
        return f"""You are CodeForge AI, an advanced autonomous coding assistant.

CORE CAPABILITIES:
You can read, write, modify files, search code, execute scripts, and integrate with Git.
You use a ReAct (Reasoning + Acting) approach: think, act, observe, iterate.

AVAILABLE TOOLS:
{self.tool_registry.list_tools()}

WORKSPACE CONTEXT:
{_clip(self.agent_state.get_context_string(), 1500)}

REASONING PROTOCOL:
1. Analyze the user's goal carefully
2. Break down complex tasks into smaller steps
3. Use tools strategically - choose the most efficient path
4. If a file is referenced as "it", "this", or "that"  use LAST MODIFIED FILE: {self.agent_state.last_modified_file or 'none'}
5. Keep track of what you've done and what remains
6. If you encounter errors, analyze and adapt your approach

OUTPUT FORMAT (strict JSON):
You must respond with EXACTLY ONE of these two formats:

Format 1 - Taking an action:
{{
    "thought": "Clear reasoning about what to do next and why",
    "action": {{
        "tool": "tool_name",
        "args": {{"required_arg": "value"}},
        "reason": "Brief explanation of why this tool"
    }}
}}

Format 2 - Final answer:
{{
    "thought": "Summary of what was accomplished",
    "final": {{
        "message": "Clear response to the user"
    }}
}}

IMPORTANT RULES:
- Never include both "action" and "final" in the same response
- Always include "thought" field with clear reasoning
- For file operations, always specify the "path" argument
- Keep responses focused on ONE next step
- If you lack information, use read_file or list_dir before acting
- Use "chat" tool for general questions not requiring file operations
- Be precise with file paths - use relative paths from workspace root
- When modifying code, preserve existing functionality unless instructed otherwise

Begin each task by thinking through the approach, then proceed step by step."""
    
    def invoke(self, prompt: str) -> dict:
        """Process a single user request through the LLM."""
        if not self.messages:
            self.messages.append({"role": "system", "content": self.system_prompt})
        
        self.messages.append({"role": "user", "content": prompt})
        
        # Convert to LangChain message format
        lc_messages = []
        for msg in self.messages:
            if msg["role"] == "system":
                lc_messages.append(SystemMessage(content=msg["content"]))
            elif msg["role"] == "user":
                lc_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                lc_messages.append(AIMessage(content=msg["content"]))
        
        # Get response from LLM
        response = self.llm.invoke(lc_messages)
        response_text = response.content
        
        self.messages.append({"role": "assistant", "content": response_text})
        
        return _parse_json(response_text)


def execute_agent_workflow(goal: str, agent: CodeForgeAgent, 
                           tool_registry: ToolRegistry, 
                           agent_state: AgentState, 
                           max_steps: int = 15) -> dict:
    """
    Execute the agent workflow using an iterative approach.
    Returns final result and execution trace.
    """
    observation = None
    execution_trace = []
    
    for step in range(max_steps):
        # Build prompt based on step
        if step == 0:
            prompt = f"Goal: {goal}\n\nAnalyze this goal and determine the first step."
        else:
            prompt = f"Observation from last action: {observation.output if observation else 'N/A'}\n\nWhat is the next step?"
        
        # Get agent decision
        response = agent.invoke(prompt)
        
        step_info = {
            "step": step + 1,
            "thought": response.get("thought", ""),
            "response": response
        }
        
        # Check if we have a final answer
        if "final" in response:
            step_info["type"] = "final"
            step_info["message"] = response["final"].get("message", "Task completed.")
            execution_trace.append(step_info)
            return {
                "success": True,
                "final_answer": response["final"].get("message"),
                "steps": execution_trace,
                "total_steps": step + 1
            }
        
        # Execute action
        if "action" in response:
            step_info["type"] = "action"
            tool_name = response["action"].get("tool")
            tool_args = response["action"].get("args", {})
            tool_reason = response["action"].get("reason", "")
            
            step_info["tool"] = tool_name
            step_info["args"] = tool_args
            step_info["reason"] = tool_reason
            
            try:
                # Get and execute tool
                tool = tool_registry.get_tool(tool_name).fn
                tool_result = tool(tool_args, tool_registry.get_context())
                
                # Update agent state
                agent_state.update_from_tool_result(tool_name, tool_args, tool_result)
                
                observation = tool_result
                step_info["result"] = {
                    "success": tool_result.ok,
                    "output": _clip(tool_result.output, 500)
                }
                
            except Exception as e:
                observation = ToolResult(ok=False, output=f"Error executing tool: {str(e)}")
                step_info["result"] = {
                    "success": False,
                    "output": str(e)
                }
        
        execution_trace.append(step_info)
    
    # Max steps reached
    return {
        "success": False,
        "final_answer": "Maximum steps reached without completing the goal.",
        "steps": execution_trace,
        "total_steps": max_steps
    }
