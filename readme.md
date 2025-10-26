# CodeForge AI 🚀# ayuverse 🔥

**CodeForge AI** is an advanced autonomous coding assistant powered by OpenAI's GPT models and built with LangChain & LangGraph orchestration. It implements an enhanced ReAct (Reasoning and Acting) methodology to help developers build, modify, and manage code projects through intelligent natural language conversations.**ayuverse** is an autonomous coding assistant powered by ReAct (Reasoning and Acting) methodology. Named after the Greek god of fire and forge, ayuverse helps you build, modify, and manage code projects through natural language conversations.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)## Demo

[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com/)

[![LangChain](https://img.shields.io/badge/LangChain-Powered-orange.svg)](https://langchain.com/)[![Watch the video](https://img.youtube.com/vi/YIwN4l4LuxI/3.jpg)](https://youtu.be/YIwN4l4LuxI?si=eUqtSghwDqh1QEZ7)

## 🌟 Key Features## About

### 🤖 Intelligent Code Generation```

- **Natural Language Interface**: Describe what you want in plain English, and CodeForge AI handles the implementation

- **Context-Aware Execution**: Maintains full workspace context and understands file relationships ▄ ▄ █ █▀ ▄▄ ▄▄▄▄▄ ▀█ ▄

- **Multi-Step Reasoning**: Breaks down complex tasks into manageable steps with transparent execution traces █ █ ▄▄▄ ▄▄▄▄ █ ▄▄ █ ██ █ █ ▄▄▄ ▄▄█▄▄ ▄ ▄ ▄▄▄

█▄▄▄▄█ █▀ █ █▀ ▀█ █▀ █ █ █ █ █ █ █ ▀ █ █ █ █ ▀

### 🛠️ Comprehensive Tool Suite █ █ █▀▀▀▀ █ █ █ █ █ █▄▄█ █ █ ▀▀▀▄ █ █ █ ▀▀▀▄

- **File Operations**: Read, write, append, and intelligently patch files █ █ ▀█▄▄▀ ██▄█▀ █ █ █ █ █ ▄▄█▄▄ █ ▀▄▄▄▀ ▀▄▄ ▀▄▄▀█ ▀▄▄▄▀

- **Code Search**: Fast text search across your entire project █ ▀▀ ▀▀

- **Script Execution**: Safely run Python scripts with built-in guardrails ▀

- **Git Integration**: Automated version control operations (add, commit, push)```

- **Web Search**: Real-time web search for up-to-date information (powered by Exa)

## ✨ Features

### 🎨 Beautiful CLI Experience

- **Rich Terminal UI**: Syntax highlighting, progress indicators, and formatted output- **Autonomous Code Generation**: Write, modify, and organize code files through natural language

- **Interactive Commands**: Powerful command palette with quick actions- **Intelligent File Operations**: Read, write, append, patch, and search files with context awareness

- **Execution Traces**: Optional detailed view of agent decision-making process- **Git Integration**: Automated version control with add, commit, and push capabilities

- **Error Recovery**: Intelligent error handling with adaptive retry strategies- **Web Search**: Real-time web search integration for up-to-date information

- **Interactive CLI**: Beautiful command-line interface with syntax highlighting and progress indicators

### 🔒 Safety First- **Context-Aware**: Maintains session context and understands file relationships

- **Path Traversal Protection**: Prevents access to parent directories- **Safety Features**: Built-in guardrails against unsafe operations

- **Destructive Operation Guards**: Built-in safeguards against unsafe operations

- **Sandboxed Execution**: Script execution with safety checks## 🚀 Quick Start

## 📦 Installation### Prerequisites

### Prerequisites1. **Python 3.8+**

- **Python 3.8 or higher**2. **API Keys** (set in `.env` file):

- **OpenAI API Key** (required) ```env

- **Exa API Key** (optional, for web search) GROQ_API_KEY=your_groq_api_key

  EXA_API_KEY=your_exa_api_key

### Quick Setup ```

1. **Clone the repository:**### Installation

   ````bash

   git clone https://github.com/yourusername/codeforge-ai.git1. Clone the repository:

   cd codeforge-ai

   ```   ```bash

   git clone <repository-url>

   ````

2. **Install dependencies:** cd

   ````bash ayuverse

   pip install -r requirements.txt   ```

   ````

3. Install dependencies:

4. **Configure environment variables:**

   `bash   `bash

   cp .env.example .env pip install groq openai python-dotenv

   `   `

   Edit `.env` and add your API keys:3. Set up your `.env` file with required API keys

   ````env

   OPENAI_API_KEY=sk-your-openai-api-key-here4. Run ayuverse:

   EXA_API_KEY=your-exa-api-key-here  # Optional   ```bash

   ```   python main.py

   ````

5. **Launch CodeForge AI:**

   ````bash## 🛠️ Available Tools

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
