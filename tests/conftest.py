"""Pytest configuration and fixtures for fb2reader tests."""

import os
import pytest
from pathlib import Path


@pytest.fixture
def test_data_dir():
    """Return the path to the test data directory."""
    return Path(__file__).parent / "test_data"


@pytest.fixture
def sample_fb2_file(test_data_dir):
    """Return the path to a sample FB2 file for testing."""
    return test_data_dir / "sample_book.fb2"


@pytest.fixture
def minimal_fb2_file(test_data_dir):
    """Return the path to a minimal valid FB2 file."""
    return test_data_dir / "minimal.fb2"


@pytest.fixture
def invalid_fb2_file(test_data_dir):
    """Return the path to an invalid FB2 file."""
    return test_data_dir / "invalid.fb2"


@pytest.fixture
def temp_output_dir(tmp_path):
    """Provide a temporary directory for output files."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir
