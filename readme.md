# 🔥 CodeForge AI — ayuverse

> **Your Intelligent AI-Powered Coding Companion**  
> Build, modify, and manage code projects using simple natural language conversations.

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Powered-orange.svg)](https://langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [📖 About](#about)
- [⭐ Key Features](#key-features)
- [🚀 Quick Start](#quick-start)
- [💻 Installation & Setup](#installation--setup)
- [🎮 Interactive Examples & Demo](#interactive-examples--demo)
- [🛠️ CLI Commands & Tools](#cli-commands--tools)
- [🧠 How It Works - The ReAct Framework](#how-it-works---the-react-framework)
- [🏗️ Project Architecture](#project-architecture)
- [⚙️ Configuration Guide](#configuration-guide)
- [🎯 Real-World Use Cases](#real-world-use-cases)
- [🔒 Security & Safety](#security--safety)
- [🤝 Contributing](#contributing)
- [📝 License](#license)
- [📧 Contact](#contact)

---

## 📖 About

**CodeForge AI** (CodeForge, or **ayuverse**) is a revolutionary autonomous coding assistant built with cutting-edge AI technologies. It combines:

- **OpenAI GPT Models** for intelligent reasoning and code generation
- **LangChain** for powerful LLM orchestration
- **LangGraph** for multi-step workflow management
- **Rich** for a beautiful terminal interface

### The Problem It Solves

Modern developers spend hours writing boilerplate code, managing files, searching for patterns, and integrating version control. CodeForge AI **automates all of this** by understanding natural language descriptions and executing complex coding tasks.

### The Solution

Instead of:

```
1. Opening multiple files
2. Writing code from scratch
3. Testing manually
4. Committing changes to git
```

You simply say:

> "Create a Python script that fetches weather data from an API and adds error handling with logging"

And CodeForge AI handles everything in seconds! ⚡

## 🌟 Key Features## About

### 🤖 Intelligent Code Generation

- **Natural Language Interface**: Describe tasks in plain English—no syntax knowledge needed
- **Context-Aware Execution**: Understands your entire project structure and file relationships
- **Multi-Step Reasoning**: Automatically breaks complex tasks into manageable steps
- **Adaptive Learning**: Remembers preferences and past interactions within a session

### 🛠️ Comprehensive Tool Suite

- **File Operations**: Read, write, append, and intelligently patch files
- **Code Search**: Regex or plain-text search across your entire project
- **Script Execution**: Safely run Python scripts with error detection
- **Git Integration**: Automated version control (add, commit, push, branching)
- **Web Search**: Real-time information fetching for current data
- **Project Analysis**: Analyze code patterns, dependencies, and architecture

### 🎨 Beautiful CLI Experience

- **Rich Terminal UI**: Syntax highlighting, progress bars, and formatted output
- **Interactive Prompts**: Intuitive command palette with smart suggestions
- **Execution Traces**: See the AI's step-by-step decision-making process
- **Error Recovery**: Intelligent handling of failures with retry strategies
- **Session History**: Track all operations performed in your session

### 🔒 Security & Safety

- **Path Validation**: Prevents unauthorized access to parent directories
- **Safe Script Execution**: Scripts are scanned for unsafe operations
- **Destructive Guards**: Built-in safeguards against accidental deletions
- **Sandboxed Execution**: All operations run in isolated environments
- **Robust Error Handling**: Graceful failure recovery and detailed error messages

## 🚀 Quick Start

Get CodeForge AI running in **less than 5 minutes**!

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, but recommended)
- OpenAI API key (get one at https://platform.openai.com/api-keys)

### Installation (Windows PowerShell)

```powershell
# 1. Clone the repository
git clone https://github.com/ayusingh-54/CodeForge-AI.git
cd CodeForge-AI

# 2. Create a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create and configure .env file
notepad .env

# 5. Add your API keys to .env

# 6. Run the application
python main.py
```

---

## 💻 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/ayusingh-54/CodeForge-AI.git
cd CodeForge-AI
```

### Step 2: Set Up Virtual Environment

```powershell
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

```bash
notepad .env  # or your favorite text editor
```

Add:

```env
OPENAI_API_KEY=sk-your-api-key-here
EXA_API_KEY=your-exa-key-here  # Optional
CODEFORGE_MODEL=gpt-4o-mini
CODEFORGE_TEMPERATURE=0.1
CODEFORGE_MAX_STEPS=20
```

### Step 5: Run the Application

````bash
python main.py
```| Tool                   | Description                       |
````

| ---------------------- | --------------------------------- |

## 🚀 Usage| `chat` | General conversation and advice |

| `read_file` | Read file contents |

### Basic Commands| `write_file` | Create or overwrite files |

| `append_file` | Append content to existing files |

Once launched, you'll see the beautiful CodeForge AI interface. Here are some special commands:| `list_dir` | List directory contents |

| `search_text_in_files` | Search for text across files |

| Command | Description || `patch_file` | Apply line-based changes to files |

|---------|-------------|| `run_python_script` | Execute Python scripts safely |

| `:help` | Display help information and available commands || `search_web` | Search the web for information |

| `:tools` | List all available tools with descriptions || `git_add` | Stage files for commit |

| `:state` | Show current agent context and workspace state || `git_commit` | Commit changes with message |

| `:clear` | Clear the terminal screen || `git_push` | Push commits to remote repository |

| `:ls [path]` | List files in directory (defaults to current) |

| `:history` | Show command history |## 💡 Usage Examples

| `:quit` or `:exit` | Exit CodeForge AI |

### Basic File Operations

### Example Tasks

```

#### Creating a New Script🔎 Enter your goal: Create a Python script that calculates fibonacci numbers and save it as fib.py

```

💬 Create a Python script that fetches weather data from an API and saves it to a JSON file

````### Code Modification



#### Code Modification```

```🔎 Enter your goal: Add error handling to the last file I created

💬 Add error handling and logging to the weather.py file```

````

### Project Setup

#### Project Setup

```

💬 Set up a Flask web application with user authentication🔎 Enter your goal: Set up a new Flask web application with routes for home and about pages

```

#### Git Operations### Git Workflow

````

💬 Add all modified files and commit with message "Add weather API integration"```

```🔎 Enter your goal: Review my changes and commit them with an appropriate message

````

#### Code Analysis

````## 🎯 CLI Commands

💬 Search for all functions that use the requests library in this project

```- `:help` - Show available commands

- `:tools` - List all available tools

## 🏗️ Architecture- `:state` - Display current agent context

- `:clear` - Clear the screen

### Core Components- `:ls [path]` - List files in directory

- `:quit` / `:exit` - Exit the application

````

codeforge-ai/## 🧠 How It Works

│

├── ayuverse/ # Main packageayuverse uses the **ReAct (Reasoning and Acting)** framework:

│ ├── core/ # Core agent logic

│ │ ├── agent.py # LangChain-based agent implementation1. **Reasoning**: The agent thinks through the problem step by step

│ │ └── state.py # Workspace state management2. **Acting**: Takes concrete actions using available tools

│ │3. **Observing**: Processes results and adjusts the approach

│ ├── tools/ # Tool implementations4. **Iterating**: Continues until the goal is achieved

│ │ ├── tools.py # Individual tool definitions

│ │ └── registry.py # Tool registry and context### Context Awareness

│ │

│ ├── ui/ # User interfaceThe agent maintains context about:

│ │ └── cli.py # Rich-powered CLI

│ │- Recently modified files

│ ├── utils/ # Utility functions- Active workspace structure

│ │ └── helpers.py # Helper functions- Previous operations and their results

│ │- Session history and patterns

│ └── config.py # Configuration management

│## 🔒 Safety Features

├── main.py # Application entry point

├── requirements.txt # Python dependencies- **Path Validation**: Prevents access to parent directories (`../`)

└── README.md # This file- **Safe Execution**: Python scripts are scanned for unsafe operations

````- **File Deletion Disabled**: Delete operations are blocked by policy

- **Error Handling**: Robust exception handling throughout the system

### Technology Stack

## ⚙️ Configuration

- **OpenAI GPT Models**: Primary language model for reasoning and code generation

- **LangChain**: Framework for building LLM applications with enhanced capabilities### Workspace Context

- **LangGraph**: Workflow orchestration and multi-step reasoning

- **Rich**: Beautiful terminal UI with colors and formattingThe agent automatically analyzes your workspace on startup, providing context about:

- **Python 3.8+**: Core programming language

- File structure and contents

## 🛠️ Available Tools- Recently modified files

- Active development patterns

| Tool | Description | Arguments |

|------|-------------|-----------|### Agent State

| `chat` | General conversation and advice | `message` |

| `read_file` | Read file contents | `path` |The system tracks:

| `write_file` | Create or overwrite files | `path`, `content` |

| `append_file` | Append content to files | `path`, `content` |- Last modified files

| `list_dir` | List directory contents | `path` (optional) |- Recently created files

| `search_text_in_files` | Search for text across files | `text`, `path` (optional) |- Current working files

| `patch_file` | Apply line-based changes | `path`, `changes` |- Session context and history

| `run_python_script` | Execute Python scripts safely | `path` |

| `search_web` | Search the web (requires Exa API) | `query` |## 🤝 Contributing

| `git_add` | Stage files for commit | `files` |

| `git_commit` | Commit changes | `message` |1. Fork the repository

| `git_push` | Push to remote repository | `remote`, `branch` |2. Create a feature branch

3. Make your changes

## ⚙️ Configuration4. Add tests if applicable

5. Submit a pull request

### Environment Variables

## 📝 License

Configure CodeForge AI through environment variables in your `.env` file:

This project is licensed under the MIT License - see the LICENSE file for details.

```env

# Required## 🙏 Acknowledgments

OPENAI_API_KEY=your-key-here

- Built with [Groq](https://groq.com/) for fast LLM inference

# Optional- Web search powered by [Exa](https://exa.ai/)

EXA_API_KEY=your-key-here- Inspired by the ReAct methodology from research papers

CODEFORGE_MODEL=gpt-4o-mini
CODEFORGE_TEMPERATURE=0.1
CODEFORGE_MAX_STEPS=20
````

### Model Configuration

You can customize the AI model behavior:

- **Model**: Default is `gpt-4o-mini` (fast and cost-effective). Can use `gpt-4o` for more complex tasks
- **Temperature**: Controls randomness (0.0 = deterministic, 1.0 = creative). Default is 0.1
- **Max Steps**: Maximum number of reasoning steps per task. Default is 20

## 🎯 Use Cases

### Web Development

- Generate boilerplate code for web frameworks
- Create API endpoints and route handlers
- Build responsive UI components

### Data Science

- Create data processing pipelines
- Generate analysis scripts
- Build visualization code

### DevOps

- Write automation scripts
- Create configuration files
- Manage deployment workflows

### Testing

- Generate unit tests
- Create test fixtures
- Build integration test suites

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for providing powerful language models
- **LangChain** team for the excellent framework
- **Rich** library for beautiful terminal interfaces
- The open-source community for inspiration and tools

## 📧 Contact

**Author**: Ayush Singh

For questions, suggestions, or issues, please open an issue on GitHub.

---

<div align="center">
  <strong>Built with ❤️ using OpenAI, LangChain, and Python</strong>
  <br>
  <sub>CodeForge AI - Your Intelligent Coding Companion</sub>
</div>
