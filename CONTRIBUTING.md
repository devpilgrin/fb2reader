# Contributing to fb2reader

Thank you for your interest in contributing to fb2reader! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project follows a Code of Conduct. By participating, you are expected to uphold this code. Please be respectful and constructive in all interactions.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:

- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Your environment (Python version, OS, etc.)
- Sample FB2 file (if applicable)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:

- A clear description of the enhancement
- Why this enhancement would be useful
- Examples of how it would work

### Pull Requests

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Install development dependencies**
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add type hints to all functions
   - Write docstrings for new functions/classes
   - Keep changes focused and atomic

4. **Add tests**
   - Write tests for new functionality
   - Ensure all tests pass
   ```bash
   pytest tests/ -v
   ```

5. **Check code quality**
   ```bash
   # Format code
   black fb2reader/ tests/

   # Lint code
   flake8 fb2reader/ tests/

   # Type check
   mypy fb2reader/
   ```

6. **Update documentation**
   - Update README.md if needed
   - Update CHANGELOG.md
   - Add docstrings to new code

7. **Commit your changes**
   ```bash
   git commit -m "Add feature: description of your changes"
   ```

8. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Open a Pull Request**
   - Provide a clear description of the changes
   - Reference any related issues
   - Wait for review and address feedback

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip
- git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/devpilgrin/fb2reader.git
   cd fb2reader
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=fb2reader --cov-report=html

# Run specific test file
pytest tests/test_fb2reader.py -v

# Run specific test
pytest tests/test_fb2reader.py::TestFB2BookInit::test_init_with_valid_file -v
```

### Code Style

This project follows:

- **PEP 8** for Python code style
- **Black** for code formatting
- **Type hints** for all functions
- **Docstrings** for all public functions/classes

### Type Hints

All functions should have type hints:

```python
def get_title(self) -> Optional[str]:
    """Get the book title."""
    ...
```

### Docstrings

Use Google-style docstrings:

```python
def example_function(param1: str, param2: int) -> bool:
    """
    Brief description of the function.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When this error occurs
    """
    ...
```

## Project Structure

```
fb2reader/
├── fb2reader/              # Main package
│   ├── __init__.py         # Package initialization
│   └── fb2reader.py        # Core implementation
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py         # Pytest fixtures
│   ├── test_fb2reader.py   # Tests
│   └── test_data/          # Test FB2 files
├── .github/
│   └── workflows/
│       └── python-publish.yml  # CI/CD configuration
├── README.md               # English documentation
├── README_RU.md            # Russian documentation
├── CHANGELOG.md            # Version history
├── CONTRIBUTING.md         # This file
├── setup.py                # Package configuration
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
└── example.py              # Usage examples
```

## Questions?

If you have questions, feel free to:

- Open an issue on GitHub
- Contact the maintainer at devpilgrim@gmail.com

Thank you for contributing! 🎉
