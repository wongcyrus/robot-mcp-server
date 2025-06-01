# robot-mcp-server

This repository contains the code for the Robot MCP (Model Context Protocol) server. It is designed to provide a backend service for robotic applications, supporting communication and control via the MCP protocol.

## Features
- Python 3.12 development environment (configured via devcontainer)
- Linting with flake8 and formatting with black
- Pytest for testing
- VS Code devcontainer support for reproducible development

## Development

### Prerequisites
- Docker (for devcontainer usage)
- VS Code with the Dev Containers extension (recommended)
- [uv](https://github.com/astral-sh/uv) (for fast Python package management)
  - Install with: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Getting Started
1. Clone this repository.
2. Open the folder in VS Code.
3. Reopen in Container when prompted (or use the Command Palette: "Dev Containers: Reopen in Container").
4. The environment will be set up automatically with Python 3.12 and all required extensions.

### Linting & Formatting
- Code is automatically formatted with [black](https://github.com/psf/black) and imports are organized with [isort](https://pycqa.github.io/isort/).
- Linting is performed with [flake8](https://flake8.pycqa.org/).

### Testing
- Tests are run using [pytest](https://docs.pytest.org/).

## Folder Structure
- `humanoid/` - Main source code for the humanoid robot server
- Additional folders may be present for other components

## License
See [LICENSE](LICENSE) for details.
