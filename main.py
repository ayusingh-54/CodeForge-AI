"""
CodeForge AI - An Intelligent Code Generation & Management System
Author: Ayush Singh
Description: Advanced AI coding assistant using LangChain/LangGraph orchestration
"""
import os
import sys
from dotenv import load_dotenv
from rich.console import Console

console = Console()

def validate_environment():
    """Validate required environment variables."""
    load_dotenv()
    
    required_vars = ["OPENAI_API_KEY"]
    optional_vars = ["EXA_API_KEY"]
    
    missing_required = [var for var in required_vars if not os.getenv(var)]
    missing_optional = [var for var in optional_vars if not os.getenv(var)]
    
    if missing_required:
        console.print("\n[bold red]❌ Missing required environment variables:[/bold red]")
        for var in missing_required:
            console.print(f"   [red]✗[/red] {var}")
        console.print("\n[yellow]Please check your .env file or set these environment variables.[/yellow]")
        console.print("[dim]Example .env file:[/dim]")
        console.print("[dim]OPENAI_API_KEY=sk-your-openai-key-here[/dim]")
        return False
    
    if missing_optional:
        console.print("\n[yellow]⚠ Optional features disabled (missing variables):[/yellow]")
        for var in missing_optional:
            console.print(f"   [yellow]![/yellow] {var}")
    
    return True

def main():
    """Main entry point for CodeForge AI."""
    console.print("[bold cyan]CodeForge AI - Intelligent Code Assistant[/bold cyan]", justify="center")
    console.print("[dim]Powered by OpenAI & LangChain[/dim]\n", justify="center")
    
    if not validate_environment():
        return 1
    
    try:
        from ayuverse.ui.cli import launch_cli
        launch_cli()
    except KeyboardInterrupt:
        console.print("\n[bold green]👋 Thank you for using CodeForge AI![/bold green]")
        return 0
    except ImportError as e:
        console.print(f"[bold red]Import error:[/bold red] {e}")
        console.print("[yellow]Run:[/yellow] pip install -r requirements.txt")
        return 1
    except Exception as e:
        console.print(f"[bold red]Unexpected error:[/bold red] {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())