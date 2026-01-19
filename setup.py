from pathlib import Path
from setuptools import setup


setup(
    name='fb2reader',
    version='1.0.4',
    author='Roman Kudryavskyi',
    author_email='devpilgrim@gmail.com',
    packages=['fb2reader'],
    url='https://github.com/devpilgrin/fb2reader',
    license='Apache-2.0',
    description='A Python library for extracting data and metadata from FB2 (FictionBook 2) format files',
    long_description_content_type='text/markdown',
    long_description=(Path(__file__).parent / "README.md").read_text(encoding='utf-8'),
    keywords=['ebook', 'metadata', 'fb2', 'fictionbook', 'parser', 'reader'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: XML',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Typing :: Typed',
    ],
    python_requires='>=3.8',
    install_requires=[
        'beautifulsoup4>=4.9.0',
        'lxml>=4.6.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=3.0.0',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/devpilgrin/fb2reader/issues',
        'Source': 'https://github.com/devpilgrin/fb2reader',
        'Documentation': 'https://github.com/devpilgrin/fb2reader#readme',
    },
)