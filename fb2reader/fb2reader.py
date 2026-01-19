"""
fb2reader - A library for extracting data and metadata from FB2 format files.

This module provides the fb2book class for parsing FB2 (FictionBook 2) files
and extracting various metadata and content elements.
"""

import os
import base64
from typing import Optional, List, Dict, Union
from bs4 import BeautifulSoup


class FB2ReaderError(Exception):
    """Base exception for fb2reader errors."""
    pass


class InvalidFB2Error(FB2ReaderError):
    """Raised when FB2 file is invalid or cannot be parsed."""
    pass


class fb2book:
    """
    A class for reading and extracting data from FB2 format files.

    This class parses FB2 (FictionBook 2) XML files and provides methods
    to extract metadata such as title, authors, description, cover images,
    and book content.

    Attributes:
        file (str): Path to the FB2 file
        soup (BeautifulSoup): Parsed XML content
        body (Optional[str]): Prettified book body HTML

    Raises:
        FileNotFoundError: If the specified file doesn't exist
        InvalidFB2Error: If the file is not a valid FB2 format
        IOError: If there's an error reading the file
    """

    def __init__(self, file: str) -> None:
        """
        Initialize fb2book instance and parse the FB2 file.

        Args:
            file: Path to the FB2 file to read

        Raises:
            FileNotFoundError: If file doesn't exist
            InvalidFB2Error: If file is not valid FB2 format
            IOError: If error reading file
        """
        self.file = file

        if not os.path.exists(file):
            raise FileNotFoundError(f"File not found: {file}")

        if not file.lower().endswith('.fb2'):
            raise InvalidFB2Error(f"File must have .fb2 extension: {file}")

        try:
            with open(file, 'r', encoding='utf-8') as fb2file:
                fb2_content = fb2file.read()
        except UnicodeDecodeError:
            raise InvalidFB2Error(f"Cannot decode file as UTF-8: {file}")
        except IOError as e:
            raise IOError(f"Error reading file: {e}")

        try:
            self.soup = BeautifulSoup(fb2_content, "xml")
        except Exception as e:
            raise InvalidFB2Error(f"Error parsing FB2 XML: {e}")

        if not self.soup.find('FictionBook'):
            raise InvalidFB2Error("Invalid FB2 format: missing FictionBook root element")

        body_elem = self.soup.find('body')
        self.body = body_elem.prettify() if body_elem else None

    def get_identifier(self) -> Optional[str]:
        """
        Extract the book identifier.

        Returns:
            Book ID string if present, None otherwise
        """
        id_elem = self.soup.find('id')
        return id_elem.text.strip() if id_elem and id_elem.text else None

    def get_title(self) -> Optional[str]:
        """
        Extract the book title.

        Returns:
            Book title string if present, None otherwise
        """
        title_elem = self.soup.find('book-title')
        return title_elem.text.strip() if title_elem and title_elem.text else None

    def get_body(self) -> Optional[str]:
        """
        Get the prettified book body content.

        Returns:
            Prettified HTML body content if present, None otherwise
        """
        return self.body

    def get_authors(self) -> List[Dict[str, Optional[str]]]:
        """
        Extract information about all book authors.

        Returns:
            List of dictionaries containing author information with keys:
            'first_name', 'middle_name', 'last_name', 'full_name'
        """
        authors = []
        for author in self.soup.find_all('author'):
            first_name_elem = author.find('first-name')
            last_name_elem = author.find('last-name')
            middle_name_elem = author.find('middle-name')

            first_name = first_name_elem.text.strip() if first_name_elem and first_name_elem.text else None
            last_name = last_name_elem.text.strip() if last_name_elem and last_name_elem.text else None
            middle_name = middle_name_elem.text.strip() if middle_name_elem and middle_name_elem.text else None

            # Build full name
            name_parts = []
            if first_name:
                name_parts.append(first_name)
            if middle_name:
                name_parts.append(middle_name)
            if last_name:
                name_parts.append(last_name)

            if name_parts:
                authors.append({
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'last_name': last_name,
                    'full_name': ' '.join(name_parts)
                })

        return authors

    def get_translators(self) -> List[Dict[str, Optional[str]]]:
        """
        Extract information about all book translators.

        Returns:
            List of dictionaries containing translator information with keys:
            'first_name', 'last_name', 'full_name'
        """
        translators = []
        for translator in self.soup.find_all('translator'):
            first_name_elem = translator.find('first-name')
            last_name_elem = translator.find('last-name')

            first_name = first_name_elem.text.strip() if first_name_elem and first_name_elem.text else None
            last_name = last_name_elem.text.strip() if last_name_elem and last_name_elem.text else None

            # Build full name
            name_parts = []
            if first_name:
                name_parts.append(first_name)
            if last_name:
                name_parts.append(last_name)

            if name_parts:
                translators.append({
                    'first_name': first_name,
                    'last_name': last_name,
                    'full_name': ' '.join(name_parts)
                })

        return translators

    def get_series(self) -> Optional[str]:
        """
        Extract the book series name.

        Returns:
            Series name if present, None otherwise
        """
        sequence = self.soup.find('sequence')
        if sequence and sequence.has_attr('name'):
            return sequence['name']
        return None

    def get_lang(self) -> Optional[str]:
        """
        Extract the book language.

        Returns:
            Language code (e.g., 'en', 'ru') if present, None otherwise
        """
        lang_elem = self.soup.find('lang')
        return lang_elem.text.strip() if lang_elem and lang_elem.text else None

    def get_description(self) -> Optional[str]:
        """
        Extract the book description/annotation.

        Returns:
            Book description text if present, None otherwise
        """
        annotation = self.soup.find('annotation')
        if annotation:
            # Get text content, preserving paragraph structure
            return annotation.get_text(separator='\n', strip=True)
        return None

    def get_tags(self) -> List[str]:
        """
        Extract all book genres/tags.

        Returns:
            List of genre strings
        """
        genres = []
        for genre in self.soup.find_all('genre'):
            if genre.text:
                genres.append(genre.text.strip())
        return genres

    def get_isbn(self) -> Optional[str]:
        """
        Extract the book ISBN.

        Returns:
            ISBN string if present, None otherwise
        """
        isbn_elem = self.soup.find('isbn')
        return isbn_elem.text.strip() if isbn_elem and isbn_elem.text else None

    def get_cover_image(self) -> Optional[BeautifulSoup]:
        """
        Get the cover image element from the FB2 file.

        Returns:
            BeautifulSoup element containing the cover image (JPEG or PNG),
            None if no cover image found
        """
        # Try JPEG first, then PNG
        cover = self.soup.find('binary', {'content-type': 'image/jpeg'})
        if not cover:
            cover = self.soup.find('binary', {'content-type': 'image/png'})
        return cover

    def save_cover_image(self, cover_image: Optional[BeautifulSoup] = None,
                        cover_image_type: Optional[str] = None,
                        output_dir: str = 'output') -> Optional[tuple]:
        """
        Save the cover image to a file.

        Args:
            cover_image: BeautifulSoup element with cover image data.
                        If None, will try to get cover using get_cover_image()
            cover_image_type: Image file extension ('jpeg' or 'png').
                             If None, will be auto-detected
            output_dir: Directory to save the image (default: 'output')

        Returns:
            Tuple of (image_name, image_type) if successful, None otherwise

        Raises:
            InvalidFB2Error: If image data is invalid or cannot be decoded
            IOError: If there's an error writing the file
        """
        # Auto-detect cover image if not provided
        if cover_image is None:
            cover_image = self.get_cover_image()

        if cover_image is None:
            return None

        # Get image metadata
        if not cover_image.has_attr('id'):
            raise InvalidFB2Error("Cover image missing 'id' attribute")

        cover_image_name = cover_image['id']
        cover_image_data = cover_image.text.strip() if cover_image.text else None

        if not cover_image_data:
            raise InvalidFB2Error("Cover image has no data")

        # Auto-detect image type if not provided
        if cover_image_type is None:
            content_type = cover_image.get('content-type', '')
            if 'jpeg' in content_type or 'jpg' in content_type:
                cover_image_type = 'jpeg'
            elif 'png' in content_type:
                cover_image_type = 'png'
            else:
                cover_image_type = 'jpeg'  # Default fallback

        # Build output path
        cover_image_path = os.path.join(output_dir, f'{cover_image_name}.{cover_image_type}')

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        try:
            # FB2 format uses base64 encoding for images
            image_bytes = base64.b64decode(cover_image_data)
            with open(cover_image_path, 'wb') as img_file:
                img_file.write(image_bytes)
        except Exception as e:
            raise InvalidFB2Error(f"Error decoding or saving cover image: {e}")

        return cover_image_name, cover_image_type

    def save_body_as_html(self, output_dir: str = 'output',
                         output_file_name: str = 'body.html') -> str:
        """
        Save the book body content as an HTML file.

        Args:
            output_dir: Directory to save the HTML file (default: 'output')
            output_file_name: Name of the output file (default: 'body.html')

        Returns:
            Path to the saved HTML file

        Raises:
            InvalidFB2Error: If body content is not available
            IOError: If there's an error writing the file
        """
        if self.body is None:
            raise InvalidFB2Error("Book body is not available")

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        body_path = os.path.join(output_dir, output_file_name)

        try:
            with open(body_path, 'w', encoding='utf-8') as html_file:
                html_file.write(self.body)
        except IOError as e:
            raise IOError(f"Error writing HTML file: {e}")

        return body_path
