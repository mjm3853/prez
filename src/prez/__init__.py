"""Prez - Presentation Builder with Python and PowerPoint integration."""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .core import PresentationBuilder
from .markdown import MarkdownParser, create_presentation_from_markdown
from .templates import SlideTemplate

__all__ = ["PresentationBuilder", "SlideTemplate", "MarkdownParser", "create_presentation_from_markdown"]
