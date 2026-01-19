"""
Unit tests for fb2reader package.
"""

import os
import pytest
from pathlib import Path
from fb2reader import fb2book, get_fb2
from fb2reader.fb2reader import FB2ReaderError, InvalidFB2Error


class TestFB2BookInit:
    """Tests for fb2book initialization."""

    def test_init_with_valid_file(self, sample_fb2_file):
        """Test initialization with a valid FB2 file."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        assert book.file == str(sample_fb2_file)
        assert book.soup is not None

    def test_init_with_nonexistent_file(self):
        """Test initialization with a non-existent file."""
        with pytest.raises(FileNotFoundError):
            fb2book("nonexistent_file.fb2")

    def test_init_with_wrong_extension(self, tmp_path):
        """Test initialization with wrong file extension."""
        wrong_file = tmp_path / "test.txt"
        wrong_file.write_text("some content")

        with pytest.raises(InvalidFB2Error):
            fb2book(str(wrong_file))

    def test_init_with_invalid_content(self, tmp_path):
        """Test initialization with invalid FB2 content."""
        invalid_fb2 = tmp_path / "invalid.fb2"
        invalid_fb2.write_text("This is not valid FB2 XML content")

        with pytest.raises(InvalidFB2Error):
            fb2book(str(invalid_fb2))


class TestFB2BookMetadata:
    """Tests for metadata extraction methods."""

    def test_get_title(self, sample_fb2_file):
        """Test getting book title."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        title = book.get_title()
        assert title is None or isinstance(title, str)

    def test_get_authors(self, sample_fb2_file):
        """Test getting book authors."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        authors = book.get_authors()
        assert isinstance(authors, list)

        for author in authors:
            assert isinstance(author, dict)
            assert 'full_name' in author
            assert 'first_name' in author
            assert 'last_name' in author

    def test_get_translators(self, sample_fb2_file):
        """Test getting book translators."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        translators = book.get_translators()
        assert isinstance(translators, list)

    def test_get_series(self, sample_fb2_file):
        """Test getting book series."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        series = book.get_series()
        assert series is None or isinstance(series, str)

    def test_get_lang(self, sample_fb2_file):
        """Test getting book language."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        lang = book.get_lang()
        assert lang is None or isinstance(lang, str)

    def test_get_description(self, sample_fb2_file):
        """Test getting book description."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        description = book.get_description()
        assert description is None or isinstance(description, str)

    def test_get_tags(self, sample_fb2_file):
        """Test getting book tags/genres."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        tags = book.get_tags()
        assert isinstance(tags, list)
        for tag in tags:
            assert isinstance(tag, str)

    def test_get_isbn(self, sample_fb2_file):
        """Test getting book ISBN."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        isbn = book.get_isbn()
        assert isbn is None or isinstance(isbn, str)

    def test_get_identifier(self, sample_fb2_file):
        """Test getting book identifier."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        identifier = book.get_identifier()
        assert identifier is None or isinstance(identifier, str)


class TestFB2BookContent:
    """Tests for content extraction methods."""

    def test_get_body(self, sample_fb2_file):
        """Test getting book body."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        body = book.get_body()
        assert body is None or isinstance(body, str)

    def test_save_body_as_html(self, sample_fb2_file, temp_output_dir):
        """Test saving book body as HTML."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))

        if book.get_body() is None:
            pytest.skip("Book has no body content")

        output_path = book.save_body_as_html(
            output_dir=str(temp_output_dir),
            output_file_name="test_body.html"
        )

        assert os.path.exists(output_path)
        assert os.path.isfile(output_path)

    def test_save_body_without_body_raises_error(self, tmp_path):
        """Test that saving body without body content raises error."""
        # Create a minimal FB2 without body
        minimal_fb2 = tmp_path / "no_body.fb2"
        minimal_fb2.write_text("""<?xml version="1.0" encoding="UTF-8"?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0">
    <description>
        <title-info>
            <book-title>Test Book</book-title>
        </title-info>
    </description>
</FictionBook>
""")

        book = fb2book(str(minimal_fb2))

        with pytest.raises(InvalidFB2Error):
            book.save_body_as_html()


class TestFB2BookCoverImage:
    """Tests for cover image extraction and saving."""

    def test_get_cover_image(self, sample_fb2_file):
        """Test getting cover image."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = fb2book(str(sample_fb2_file))
        cover = book.get_cover_image()

        # Cover may or may not exist, just check type
        assert cover is None or hasattr(cover, 'name')

    def test_save_cover_image_without_cover_returns_none(self, tmp_path):
        """Test saving cover when no cover exists returns None."""
        minimal_fb2 = tmp_path / "no_cover.fb2"
        minimal_fb2.write_text("""<?xml version="1.0" encoding="UTF-8"?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0">
    <description>
        <title-info>
            <book-title>Test Book</book-title>
        </title-info>
    </description>
    <body>
        <section>
            <p>Test content</p>
        </section>
    </body>
</FictionBook>
""")

        book = fb2book(str(minimal_fb2))
        result = book.save_cover_image()
        assert result is None


class TestGetFB2Function:
    """Tests for the get_fb2 helper function."""

    def test_get_fb2_with_valid_file(self, sample_fb2_file):
        """Test get_fb2 with a valid FB2 file."""
        if not sample_fb2_file.exists():
            pytest.skip("Sample FB2 file not found")

        book = get_fb2(str(sample_fb2_file))
        assert book is not None
        assert isinstance(book, fb2book)

    def test_get_fb2_with_wrong_extension(self):
        """Test get_fb2 with wrong file extension returns None."""
        result = get_fb2("test.txt")
        assert result is None

    def test_get_fb2_with_none(self):
        """Test get_fb2 with None returns None."""
        result = get_fb2(None)
        assert result is None


class TestMinimalFB2:
    """Tests with a minimal valid FB2 structure."""

    @pytest.fixture
    def minimal_fb2(self, tmp_path):
        """Create a minimal valid FB2 file."""
        fb2_file = tmp_path / "minimal.fb2"
        fb2_file.write_text("""<?xml version="1.0" encoding="UTF-8"?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0">
    <description>
        <title-info>
            <genre>fiction</genre>
            <author>
                <first-name>John</first-name>
                <middle-name>Q</middle-name>
                <last-name>Doe</last-name>
            </author>
            <book-title>Test Book Title</book-title>
            <annotation>This is a test book description.</annotation>
            <lang>en</lang>
            <sequence name="Test Series"/>
        </title-info>
        <document-info>
            <id>test-id-123</id>
        </document-info>
        <publish-info>
            <isbn>123-456-789</isbn>
        </publish-info>
    </description>
    <body>
        <section>
            <title><p>Chapter 1</p></title>
            <p>This is the content of chapter 1.</p>
        </section>
    </body>
</FictionBook>
""")
        return fb2_file

    def test_minimal_fb2_parsing(self, minimal_fb2):
        """Test parsing a minimal FB2 file."""
        book = fb2book(str(minimal_fb2))

        assert book.get_title() == "Test Book Title"
        assert book.get_identifier() == "test-id-123"
        assert book.get_isbn() == "123-456-789"
        assert book.get_lang() == "en"
        assert book.get_series() == "Test Series"
        assert "fiction" in book.get_tags()

        authors = book.get_authors()
        assert len(authors) == 1
        assert authors[0]['first_name'] == "John"
        assert authors[0]['middle_name'] == "Q"
        assert authors[0]['last_name'] == "Doe"
        assert authors[0]['full_name'] == "John Q Doe"

        description = book.get_description()
        assert "test book description" in description.lower()

        body = book.get_body()
        assert body is not None
        assert "Chapter 1" in body
