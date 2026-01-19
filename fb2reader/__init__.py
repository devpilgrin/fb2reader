from .fb2reader import fb2book

__all__ = ['fb2book', 'get_fb2']


def get_fb2(file):
    """
    Create and return an fb2book instance from a file path.

    Args:
        file: Path to the FB2 file

    Returns:
        fb2book: An instance of fb2book class if file is valid FB2
        None: If file is not an FB2 file

    Raises:
        FileNotFoundError: If file does not exist
        ValueError: If file is not a valid FB2 format
    """
    if file and file.lower().endswith('.fb2'):
        return fb2book(file)
    return None

