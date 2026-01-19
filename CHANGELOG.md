# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4] - TBD

### Fixed
- **CRITICAL**: Fixed `_get_file()` function in `__init__.py` that was incorrectly setting `file = None` before checking it
- **CRITICAL**: Fixed `get_fb2()` function not returning the result
- **CRITICAL**: Fixed `save_cover_image()` missing `self` parameter
- **CRITICAL**: Fixed cover image decoding from hex to base64 (FB2 uses base64 encoding)
- Fixed authors and translators returning sets instead of strings
- Fixed `middle_name` concatenation causing TypeError when None
- Fixed file opening mode from 'r+' to 'r' (read-only)
- Fixed inconsistent return types in author/translator methods

### Added
- Comprehensive error handling with custom exceptions (`FB2ReaderError`, `InvalidFB2Error`)
- Type hints for all methods and functions
- Detailed docstrings for all classes and methods
- File validation (existence, extension, UTF-8 encoding, valid XML)
- FB2 format validation (checks for FictionBook root element)
- Comprehensive test suite with pytest
- Test coverage for all major functionality
- Test data files for automated testing
- CI/CD workflow with automated testing before publishing
- Support for Python 3.8 through 3.12
- requirements.txt and requirements-dev.txt files
- Complete API documentation in README
- Russian language README (README_RU.md)
- Improved example.py with comprehensive usage examples

### Changed
- Updated CI/CD workflow to run tests before publishing
- CI/CD now only triggers on version tags (v*) instead of every push
- Improved author/translator data structure (now returns dictionaries with separate fields)
- Updated dependencies with minimum version requirements
- Improved project metadata in setup.py
- Updated .gitignore to include .idea/ and output/ directories
- Enhanced description extraction to preserve paragraph structure

### Removed
- Removed unnecessary dependencies from CI/CD workflow (pyyaml, python-daemon, obd)
- Removed support for Python < 3.8

## [1.0.3] - 2024

### Changed
- Bug fixes and compatibility improvements
- Updated setup.py configuration

## [1.0.2] - 2024

### Changed
- Initial stable release
- Basic FB2 reading functionality

## [1.0.1] - 2024

### Added
- Initial release
- Basic metadata extraction
- Cover image extraction
- Book body extraction

[1.0.4]: https://github.com/devpilgrin/fb2reader/compare/v1.0.3...v1.0.4
[1.0.3]: https://github.com/devpilgrin/fb2reader/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/devpilgrin/fb2reader/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/devpilgrin/fb2reader/releases/tag/v1.0.1
