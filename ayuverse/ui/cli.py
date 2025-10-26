"""
CodeForge AI CLI - Beautiful command-line interface using Rich
Author: Ayush Singh
"""
import os
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.prompt import Prompt
from rich import box
import time

from ..tools import tool_registry, ToolRegistry
from ..core.state import AgentState
from ..core.agent import CodeForgeAgent, execute_agent_workflow

# Initialize Rich console
console = Console()


def display_banner():
    """Display the CodeForge AI banner."""
    console.clear()
    
    # Create a centered banner panel
    banner_content = """
[bold cyan]
  ██████╗ ██████╗ ██████╗ ███████╗███████╗ ██████╗ ██████╗ ███████╗
 ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
 ██║     ██║   ██║██║  ██║█████╗  █████╗  ██║   ██║██████╔╝█████╗  
 ██║     ██║   ██║██║  ██║██╔══╝  ██╔══╝  ██║   ██║██╔══██╗██╔══╝  
 ╚██████╗╚██████╔╝██████╔╝███████╗██║     ╚██████╔╝██║  ██║███████╗
  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝
[/bold cyan]

[bold white]                    🤖 AI-Powered Code Assistant 🤖[/bold white]
[dim cyan]              Intelligent • Autonomous • Efficient[/dim cyan]
"""
    
    banner_panel = Panel(
        banner_content,
        border_style="bold cyan",
        box=box.DOUBLE,
        padding=(1, 2),
    )
    
    console.print("\n")
    console.print(banner_panel, justify="center")
    console.print("\n[dim cyan]Powered by OpenAI & LangChain[/dim cyan]\n", justify="center")


def display_help():
    """Display help information."""
    help_table = Table(
        title="[bold cyan]⚡ Available Commands[/bold cyan]", 
        box=box.DOUBLE, 
        show_header=True, 
        header_style="bold magenta",
        border_style="cyan",
        title_style="bold cyan"
    )
    help_table.add_column("Command", style="cyan bold", width=20, justify="left")
    help_table.add_column("Description", style="white", width=60)
    
    commands = [
        (":help", "Display this help message with all available commands"),
        (":tools", "List all available tools with detailed descriptions"),
        (":state", "Show current agent context and workspace information"),
        (":clear", "Clear the terminal screen and show banner"),
        (":ls [path]", "List files and directories (defaults to current directory)"),
        (":history", "Show command history for this session"),
        (":quit / :exit", "Exit CodeForge AI gracefully"),
    ]
    
    for cmd, desc in commands:
        help_table.add_row(cmd, desc)
    
    console.print()
    console.print(help_table, justify="center")
    console.print()
    console.print(
        Panel(
            "[bold yellow]💡 Pro Tips:[/bold yellow]\n\n"
            "• Just describe what you want in plain English!\n"
            "• I understand context - say 'modify it' to edit the last file\n"
            "• Use :state to see what files I'm tracking\n"
            "• Press Ctrl+C to interrupt long operations",
            border_style="yellow",
            box=box.ROUNDED,
            padding=(1, 2)
        ),
        justify="center"
    )
    console.print()


def display_tools(tool_registry: ToolRegistry):
    """Display available tools in a formatted table."""
    tools_table = Table(
        title="[bold green]🛠️  Available Tools[/bold green]", 
        box=box.DOUBLE, 
        show_header=True,
        header_style="bold green",
        border_style="green",
        title_style="bold green"
    )
    tools_table.add_column("#", style="dim", width=4, justify="center")
    tools_table.add_column("Tool Name", style="cyan bold", width=20)
    tools_table.add_column("Description", style="white", width=60)
    
    for idx, (name, tool) in enumerate(tool_registry.tools.items(), 1):
        tools_table.add_row(str(idx), name, tool.description)
    
    console.print()
    console.print(tools_table, justify="center")
    console.print()


def display_agent_state(agent_state: AgentState):
    """Display current agent state and context."""
    state_content = agent_state.get_context_string() or "[dim]No recent activity[/dim]"
    
    state_panel = Panel(
        state_content,
        title="[bold blue]📊 Agent State & Workspace Context[/bold blue]",
        border_style="blue",
        box=box.DOUBLE,
        padding=(1, 2)
    )
    console.print()
    console.print(state_panel, justify="center")
    console.print()


def display_execution_trace(result: dict):
    """Display the execution trace in a beautiful format."""
    console.print("\n" + "="*70)
    console.print("📝 [bold cyan]Execution Trace[/bold cyan]")
    console.print("="*70 + "\n")
    
    for step_info in result.get("steps", []):
        step_num = step_info.get("step", "?")
        thought = step_info.get("thought", "")
        step_type = step_info.get("type", "unknown")
        
        # Step header
        console.print(f"\n[bold yellow]Step {step_num}:[/bold yellow]", style="bold")
        
        # Thought
        if thought:
            console.print(f"  [dim]💭 Thought:[/dim] {thought}")
        
        # Action details
        if step_type == "action":
            tool = step_info.get("tool", "unknown")
            reason = step_info.get("reason", "")
            result_info = step_info.get("result", {})
            
            console.print(f"  [cyan]🔧 Tool:[/cyan] {tool}")
            if reason:
                console.print(f"  [dim]📋 Reason:[/dim] {reason}")
            
            if result_info:
                success = result_info.get("success", False)
                output = result_info.get("output", "")
                
                if success:
                    console.print(f"  [green]✓ Result:[/green]")
                else:
                    console.print(f"  [red]✗ Error:[/red]")
                
                if output:
                    # Truncate long outputs
                    if len(output) > 300:
                        output = output[:300] + "...[truncated]"
                    console.print(Panel(output, border_style="dim", box=box.MINIMAL))
        
        # Final answer
        elif step_type == "final":
            message = step_info.get("message", "")
            console.print(f"\n[bold green]✓ Final Answer:[/bold green]")
            console.print(Panel(message, border_style="green", box=box.DOUBLE))
    
    console.print("\n" + "="*70 + "\n")


def handle_command(cmd: str, tool_registry: ToolRegistry, 
                   agent_state: AgentState) -> Optional[str]:
    """Handle special commands. Returns 'EXIT' if should quit, None otherwise."""
    parts = cmd.split(maxsplit=1)
    command = parts[0].lower()
    
    if command in (":quit", ":exit"):
        return "EXIT"
    
    if command == ":help":
        display_help()
        return None
    
    if command == ":tools":
        display_tools(tool_registry)
        return None
    
    if command == ":state":
        display_agent_state(agent_state)
        return None
    
    if command == ":clear":
        os.system("cls" if os.name == "nt" else "clear")
        display_banner()
        return None
    
    if command == ":ls":
        path = parts[1] if len(parts) > 1 else "."
        tool = tool_registry.get_tool("list_dir").fn
        res = tool({"path": path}, tool_registry.get_context())
        
        if res.ok:
            console.print(Panel(res.output, title=f"📁 {path}", border_style="cyan"))
        else:
            console.print(f"[red]Error:[/red] {res.output}")
        return None
    
    console.print(f"[red]Unknown command:[/red] {cmd}")
    console.print("[yellow]Type :help for available commands[/yellow]")
    return None


def launch_cli():
    """Main CLI entry point."""
    display_banner()
    
    # Welcome message in a centered panel
    welcome_panel = Panel(
        "[bold green]🚀 Welcome to CodeForge AI![/bold green]\n\n"
        "Type [cyan]:help[/cyan] for commands or describe your coding goal in natural language.\n"
        "I can help you write code, modify files, search projects, and much more!",
        title="[bold cyan]Getting Started[/bold cyan]",
        border_style="green",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    console.print(welcome_panel, justify="center")
    console.print()
    
    # Initialize components
    session_agent_state = AgentState()
    agent = CodeForgeAgent(tool_registry, agent_state=session_agent_state)
    
    command_history = []
    
    while True:
        try:
            # Get user input with Rich prompt
            goal = Prompt.ask("\n[bold blue]💬 What would you like me to do?[/bold blue]")
            
            if not goal.strip():
                continue
            
            command_history.append(goal)
            
            # Handle special commands
            if goal.startswith(":"):
                result = handle_command(goal, tool_registry, session_agent_state)
                if result == "EXIT":
                    console.print("\n[bold cyan]👋 Thank you for using CodeForge AI![/bold cyan]")
                    console.print("[dim]Goodbye! 🚀[/dim]\n")
                    break
                continue
            
            # Execute agent workflow
            console.print()
            console.print(Panel(
                "⚡ [yellow]Processing your request...[/yellow]\n"
                "🧠 [dim]Analyzing, planning, and executing...[/dim]",
                border_style="yellow",
                box=box.ROUNDED
            ), justify="center")
            console.print()
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                task = progress.add_task("🧠 Thinking and executing...", total=None)
                
                result = execute_agent_workflow(
                    goal, agent, tool_registry, session_agent_state, max_steps=20
                )
            
            # Display results
            console.print()
            if result.get("success"):
                result_panel = Panel(
                    f"[bold green]✓ Task Completed Successfully![/bold green]\n\n"
                    f"{result.get('final_answer', 'Done!')}",
                    title="[bold green]📋 Result[/bold green]",
                    border_style="green",
                    box=box.DOUBLE,
                    padding=(1, 2)
                )
                console.print(result_panel, justify="center")
            else:
                result_panel = Panel(
                    f"[bold yellow]⚠ Task Incomplete[/bold yellow]\n\n"
                    f"{result.get('final_answer', 'Maximum steps reached')}",
                    title="[bold yellow]⚠️  Status[/bold yellow]",
                    border_style="yellow",
                    box=box.ROUNDED,
                    padding=(1, 2)
                )
                console.print(result_panel, justify="center")
            console.print()
            
            # Show execution trace
            console.print(f"[dim]Steps taken: {result.get('total_steps', 0)}[/dim]", justify="center")
            
            # Ask if user wants to see detailed trace
            show_trace = Prompt.ask(
                "\n[dim]📊 Show detailed execution trace?[/dim]",
                choices=["y", "n"],
                default="n"
            )
            
            if show_trace.lower() == "y":
                display_execution_trace(result)
        
        except KeyboardInterrupt:
            console.print("\n")
            interrupt_panel = Panel(
                "[yellow]⚠ Interrupted by user[/yellow]\n\n"
                "Would you like to exit CodeForge AI?",
                border_style="yellow",
                box=box.ROUNDED,
                padding=(1, 2)
            )
            console.print(interrupt_panel, justify="center")
            
            should_quit = Prompt.ask(
                "\n[bold]Exit?[/bold]",
                choices=["y", "n"],
                default="n"
            )
            if should_quit.lower() == "y":
                console.print()
                goodbye_panel = Panel(
                    "[bold cyan]👋 Thank you for using CodeForge AI![/bold cyan]\n\n"
                    "[dim]Happy coding! 🚀[/dim]",
                    border_style="cyan",
                    box=box.DOUBLE,
                    padding=(1, 2)
                )
                console.print(goodbye_panel, justify="center")
                console.print()
                break
        
        except Exception as e:
            console.print()
            error_panel = Panel(
                f"[bold red]❌ An error occurred:[/bold red]\n\n"
                f"[red]{str(e)}[/red]\n\n"
                f"[dim]Type :help for assistance or :quit to exit[/dim]",
                border_style="red",
                box=box.ROUNDED,
                padding=(1, 2)
            )
            console.print(error_panel, justify="center")
            console.print()


if __name__ == "__main__":
    launch_cli()
