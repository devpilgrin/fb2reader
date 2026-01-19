"""
Example usage of fb2reader library.

This script demonstrates how to use fb2reader to extract metadata
and content from FB2 files.
"""

import sys
import io

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from fb2reader import fb2book, get_fb2
from fb2reader.fb2reader import InvalidFB2Error, FB2ReaderError

# Path to the FB2 file
file_path = 'test.fb2'

print("=" * 60)
print("fb2reader Library - Usage Example")
print("=" * 60)

try:
    # Create fb2book instance
    print(f"\nOpening file: {file_path}")
    book = fb2book(file_path)
    print("[OK] File opened successfully\n")

    # Extract and display metadata
    print("-" * 60)
    print("BOOK METADATA")
    print("-" * 60)

    # Basic information
    title = book.get_title()
    print(f"Title: {title}")

    isbn = book.get_isbn()
    print(f"ISBN: {isbn}")

    identifier = book.get_identifier()
    print(f"Identifier: {identifier}")

    lang = book.get_lang()
    print(f"Language: {lang}")

    series = book.get_series()
    if series:
        print(f"Series: {series}")

    # Authors
    print("\nAuthors:")
    authors = book.get_authors()
    if authors:
        for i, author in enumerate(authors, 1):
            print(f"  {i}. {author['full_name']}")
            if author.get('first_name'):
                print(f"     First name: {author['first_name']}")
            if author.get('middle_name'):
                print(f"     Middle name: {author['middle_name']}")
            if author.get('last_name'):
                print(f"     Last name: {author['last_name']}")
    else:
        print("  No authors found")

    # Translators
    translators = book.get_translators()
    if translators:
        print("\nTranslators:")
        for i, translator in enumerate(translators, 1):
            print(f"  {i}. {translator['full_name']}")

    # Genres/Tags
    tags = book.get_tags()
    if tags:
        print(f"\nGenres/Tags: {', '.join(tags)}")

    # Description
    description = book.get_description()
    if description:
        print(f"\nDescription:")
        # Limit description to first 200 characters for display
        if len(description) > 200:
            print(f"  {description[:200]}...")
        else:
            print(f"  {description}")

    # Content information
    print("\n" + "-" * 60)
    print("CONTENT INFORMATION")
    print("-" * 60)

    body = book.get_body()
    if body:
        print(f"Body length: {len(body)} characters")
    else:
        print("No body content found")

    # Cover image
    cover = book.get_cover_image()
    if cover:
        print("Cover image: Found")
        # Uncomment to save cover image
        # result = book.save_cover_image(output_dir='output')
        # if result:
        #     image_name, image_type = result
        #     print(f"  Cover saved as: {image_name}.{image_type}")
    else:
        print("Cover image: Not found")

    # Uncomment to save body as HTML
    # if body:
    #     output_path = book.save_body_as_html(
    #         output_dir='output',
    #         output_file_name='book_body.html'
    #     )
    #     print(f"\nBody saved to: {output_path}")

    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)

except FileNotFoundError:
    print(f"\n[ERROR] Error: File '{file_path}' not found")
    print("Please make sure the file exists in the current directory")

except InvalidFB2Error as e:
    print(f"\n[ERROR] Invalid FB2 file: {e}")
    print("The file may be corrupted or not a valid FB2 format")

except FB2ReaderError as e:
    print(f"\n[ERROR] FB2 Reader error: {e}")

except Exception as e:
    print(f"\n[ERROR] Unexpected error: {e}")

print()

# Alternative method using get_fb2 helper function
print("\n" + "=" * 60)
print("Alternative: Using get_fb2() Helper Function")
print("=" * 60)

book2 = get_fb2(file_path)
if book2:
    print(f"[OK] Successfully opened: {book2.get_title()}")
else:
    print("[ERROR] Failed to open file (not a valid FB2 file)")
