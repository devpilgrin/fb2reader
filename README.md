# fb2reader

[![PyPI version](https://badge.fury.io/py/fb2reader.svg)](https://badge.fury.io/py/fb2reader)
[![Python versions](https://img.shields.io/pypi/pyversions/fb2reader.svg)](https://pypi.org/project/fb2reader/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[Русская версия](README_RU.md) | English

A Python library for extracting data and metadata from FB2 (FictionBook 2) format files.

## Description

**fb2reader** is a lightweight and easy-to-use Python library designed for working with FB2 format files. It provides convenient methods for extracting book metadata (title, authors, description, ISBN, etc.) and content, making it ideal for building e-book management systems, cataloging tools, or reading applications.

## Features

- Extract book metadata:
  - Title, authors, translators
  - Book series information
  - Language, genres/tags
  - ISBN, book identifier
  - Description/annotation
- Extract and save cover images (JPEG/PNG)
- Extract book body content
- Save book content as HTML
- Full error handling and validation
- Type hints support
- Comprehensive test coverage
- Support for Python 3.8+

## Installation

Install using pip:

```bash
pip install fb2reader
```

### Requirements

- Python 3.8 or higher
- BeautifulSoup4
- lxml

## Quick Start

```python
from fb2reader import fb2book

# Open an FB2 file
book = fb2book('path/to/your/book.fb2')

# Get book metadata
title = book.get_title()
authors = book.get_authors()
description = book.get_description()

print(f"Title: {title}")
print(f"Authors: {authors}")
print(f"Description: {description}")
```

## Usage Examples

### Getting Book Metadata

```python
from fb2reader import fb2book

book = fb2book('example.fb2')

# Get basic information
title = book.get_title()
isbn = book.get_isbn()
lang = book.get_lang()
identifier = book.get_identifier()

# Get authors (returns list of dicts)
authors = book.get_authors()
for author in authors:
    print(f"Author: {author['full_name']}")
    print(f"  First name: {author['first_name']}")
    print(f"  Last name: {author['last_name']}")

# Get translators
translators = book.get_translators()
for translator in translators:
    print(f"Translator: {translator['full_name']}")

# Get series information
series = book.get_series()
if series:
    print(f"Part of series: {series}")

# Get genres/tags
tags = book.get_tags()
print(f"Genres: {', '.join(tags)}")

# Get description
description = book.get_description()
print(f"Description: {description}")
```

### Working with Cover Images

```python
from fb2reader import fb2book

book = fb2book('example.fb2')

# Check if book has a cover
cover = book.get_cover_image()
if cover:
    # Save cover image
    result = book.save_cover_image(output_dir='covers')
    if result:
        image_name, image_type = result
        print(f"Cover saved: {image_name}.{image_type}")
else:
    print("No cover image found")

# You can also specify the image type explicitly
book.save_cover_image(
    cover_image=cover,
    cover_image_type='jpeg',
    output_dir='my_covers'
)
```

### Extracting Book Content

```python
from fb2reader import fb2book

book = fb2book('example.fb2')

# Get book body as string
body = book.get_body()
if body:
    print(f"Body length: {len(body)} characters")

# Save book body as HTML file
try:
    output_path = book.save_body_as_html(
        output_dir='output',
        output_file_name='book_content.html'
    )
    print(f"Content saved to: {output_path}")
except Exception as e:
    print(f"Error saving content: {e}")
```

### Using the Helper Function

```python
from fb2reader import get_fb2

# Alternative way to create fb2book instance
book = get_fb2('example.fb2')

if book:
    title = book.get_title()
    print(f"Title: {title}")
else:
    print("Invalid or non-FB2 file")
```

### Error Handling

```python
from fb2reader import fb2book
from fb2reader.fb2reader import InvalidFB2Error, FB2ReaderError

try:
    book = fb2book('example.fb2')
    title = book.get_title()
    print(f"Title: {title}")

except FileNotFoundError:
    print("File not found")
except InvalidFB2Error as e:
    print(f"Invalid FB2 file: {e}")
except FB2ReaderError as e:
    print(f"FB2 Reader error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## API Reference

### Class: `fb2book`

Main class for working with FB2 files.

#### Constructor

```python
fb2book(file: str)
```

- `file` (str): Path to the FB2 file

**Raises:**
- `FileNotFoundError`: If file doesn't exist
- `InvalidFB2Error`: If file is not a valid FB2 format
- `IOError`: If there's an error reading the file

#### Methods

##### Metadata Methods

- `get_identifier() -> Optional[str]` - Get book identifier
- `get_title() -> Optional[str]` - Get book title
- `get_authors() -> List[Dict[str, Optional[str]]]` - Get list of authors
- `get_translators() -> List[Dict[str, Optional[str]]]` - Get list of translators
- `get_series() -> Optional[str]` - Get series name
- `get_lang() -> Optional[str]` - Get language code
- `get_description() -> Optional[str]` - Get book description/annotation
- `get_tags() -> List[str]` - Get list of genres/tags
- `get_isbn() -> Optional[str]` - Get ISBN

##### Content Methods

- `get_body() -> Optional[str]` - Get book body content
- `get_cover_image() -> Optional[BeautifulSoup]` - Get cover image element
- `save_cover_image(cover_image=None, cover_image_type=None, output_dir='output') -> Optional[tuple]` - Save cover image
- `save_body_as_html(output_dir='output', output_file_name='body.html') -> str` - Save body as HTML

### Function: `get_fb2`

```python
get_fb2(file: str) -> Optional[fb2book]
```

Helper function to create fb2book instance.

- Returns `fb2book` instance if file is valid FB2
- Returns `None` if file is not an FB2 file

### Exceptions

- `FB2ReaderError` - Base exception for all fb2reader errors
- `InvalidFB2Error` - Raised when FB2 file is invalid or cannot be parsed

## Development

### Running Tests

```bash
# Install development dependencies
pip install -e .
pip install pytest pytest-cov

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=fb2reader --cov-report=html
```

### Project Structure

```
fb2reader/
├── fb2reader/           # Main package
│   ├── __init__.py      # Package initialization
│   └── fb2reader.py     # Core implementation
├── tests/               # Test suite
│   ├── __init__.py
│   ├── conftest.py      # Pytest fixtures
│   ├── test_fb2reader.py
│   └── test_data/       # Test FB2 files
├── README.md            # Documentation (English)
├── README_RU.md         # Documentation (Russian)
├── setup.py             # Package configuration
├── requirements.txt     # Dependencies
└── LICENSE              # Apache 2.0 License
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Author

Roman Kudryavskyi - [devpilgrim@gmail.com](mailto:devpilgrim@gmail.com)

## Links

- [PyPI Package](https://pypi.org/project/fb2reader/)
- [GitHub Repository](https://github.com/devpilgrin/fb2reader)
- [Issue Tracker](https://github.com/devpilgrin/fb2reader/issues)

## Changelog

### Version 1.0.4 (Upcoming)

- Fixed critical bugs in `__init__.py`
- Fixed cover image decoding (base64 instead of hex)
- Added proper error handling and validation
- Added type hints to all methods
- Improved docstrings
- Added comprehensive test suite
- Updated CI/CD pipeline with automated testing
- Improved documentation

### Version 1.0.3

- Bug fixes and compatibility improvements

## Acknowledgments

- FB2 format specification: [FictionBook](http://www.fictionbook.org/)
- Built with [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
