"""
CodeForge AI Configuration
Centralized configuration management
Author: Ayush Singh
"""
import os
from typing import Optional
from dataclasses import dataclass


@dataclass
class CodeForgeConfig:
    """Configuration class for CodeForge AI."""
    
    # Model configuration
    model_name: str = "gpt-4o-mini"
    temperature: float = 0.1
    max_tokens: Optional[int] = None
    
    # Execution limits
    max_steps: int = 20
    max_file_size: int = 8192
    max_workspace_files: int = 50
    
    # API Keys
    openai_api_key: Optional[str] = None
    exa_api_key: Optional[str] = None
    
    # Workspace settings
    workspace_path: str = "."
    ignore_dirs: set = None
    priority_extensions: set = None
    
    # UI settings
    show_detailed_trace: bool = False
    color_output: bool = True
    
    def __post_init__(self):
        """Initialize default values."""
        if self.ignore_dirs is None:
            self.ignore_dirs = {
                ".git", ".github", "__pycache__", "node_modules", 
                ".venv", "venv", "env", ".env", "dist", "build", 
                ".next", "coverage", ".pytest_cache"
            }
        
        if self.priority_extensions is None:
            self.priority_extensions = {
                ".py", ".js", ".ts", ".jsx", ".tsx", ".md", 
                ".json", ".yaml", ".yml", ".toml", ".cfg", 
                ".ini", ".txt", ".html", ".css", ".sh"
            }
        
        # Load API keys from environment if not set
        if not self.openai_api_key:
            self.openai_api_key = os.getenv("OPENAI_API_KEY")
        
        if not self.exa_api_key:
            self.exa_api_key = os.getenv("EXA_API_KEY")
    
    @classmethod
    def from_env(cls) -> "CodeForgeConfig":
        """Create configuration from environment variables."""
        return cls(
            model_name=os.getenv("CODEFORGE_MODEL", "gpt-4o-mini"),
            temperature=float(os.getenv("CODEFORGE_TEMPERATURE", "0.1")),
            max_steps=int(os.getenv("CODEFORGE_MAX_STEPS", "20")),
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            exa_api_key=os.getenv("EXA_API_KEY"),
        )


# Global config instance
config = CodeForgeConfig.from_env()
