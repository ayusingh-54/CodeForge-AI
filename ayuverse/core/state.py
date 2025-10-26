"""
CodeForge AI State Management - Enhanced workspace context tracking
Author: Ayush Singh
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from pathlib import Path
import os

from ayuverse.tools.registry import ToolResult
from ayuverse.utils.helpers import _clip


# ========== Workspace Analysis ==========
def analyze_workspace(workspace_path: str, max_file_size: int = 8192, 
                     max_files: int = 50) -> str:
    """
    Enhanced workspace scanner with intelligent file filtering.
    Returns a comprehensive summary of important files and their contents.
    """
    summary = []
    file_count = 0
    
    # Directories to ignore
    ignore_dirs = {".git", ".github", "__pycache__", "node_modules", ".venv", 
                  "venv", "env", ".env", "dist", "build", ".next", "coverage"}
    
    # File extensions to prioritize
    priority_extensions = {".py", ".js", ".ts", ".jsx", ".tsx", ".md", ".json", 
                          ".yaml", ".yml", ".toml", ".cfg", ".ini"}
    
    for root, dirs, files in os.walk(workspace_path):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        rel_root = os.path.relpath(root, workspace_path)
        if any(skip in rel_root.split(os.sep) for skip in ignore_dirs):
            continue
        
        for file in files:
            if file_count >= max_files:
                summary.append(f"\n... (additional files omitted for brevity)")
                return "\n".join(summary)
            
            # Skip hidden and compiled files
            if file.startswith(".") or file.endswith((".pyc", ".pyo", ".so", ".dll")):
                continue
            
            file_path = os.path.join(root, file)
            rel_path = os.path.join(rel_root, file) if rel_root != "." else file
            file_ext = Path(file).suffix
            
            # Check if this is a priority file
            if file_ext not in priority_extensions:
                summary.append(f"{rel_path} (skipped - not prioritized)")
                continue
            
            try:
                size = os.path.getsize(file_path)
                if size > max_file_size:
                    summary.append(f"{rel_path} ({size} bytes - too large, skipped)")
                else:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read(max_file_size)
                    summary.append(f"📄 {rel_path}:\n{_clip(content, 1000)}\n---")
                    file_count += 1
            except Exception as e:
                summary.append(f"{rel_path} (error: {e})")
    
    return "\n".join(summary) if summary else "Empty workspace"

@dataclass
class AgentState:
    last_modified_file: Optional[str] = None
    recently_created_files: List[str] = field(default_factory=list)
    current_files: Dict[str, str] = field(default_factory=dict)
    session_context: str = ""
    workspace_context: str = analyze_workspace(workspace_path = "./")

    last_topic: Optional[str] = None
    last_answer: Optional[str] = None

    
    def update_from_tool_result(self, tool_name: str, args: dict, result: ToolResult):
        """Update state based on tool execution"""
        if tool_name in ["write_file", "patch_file", "append_file"] and result.ok:
            file_path = args.get("path")
            if file_path:
                self.last_modified_file = file_path
                self.current_files[file_path] = tool_name
                
        elif tool_name == "write_file" and result.ok:
            file_path = args.get("path")
            if file_path and file_path not in self.current_files:
                self.recently_created_files.append(file_path)
    
    def get_context_string(self) -> str:
        context_parts = []

        if self.workspace_context:
            context_parts.append(f"WORKSPACE CONTEXT:\n{_clip(self.workspace_context, 1000)}")
        
        if self.last_modified_file:
            context_parts.append(f"LAST MODIFIED FILE: {self.last_modified_file}")
            
        if self.recently_created_files:
            context_parts.append(f"RECENTLY CREATED: {', '.join(self.recently_created_files[-3:])}")
            
        if self.current_files:
            active_files = list(self.current_files.keys())[-3:]
            context_parts.append(f"ACTIVE FILES: {', '.join(active_files)}")
        if self.last_topic:
            context_parts.append(f"LAST TOPIC: {self.last_topic}")
            
        return "\n".join(context_parts) if context_parts else "No recent file operations"