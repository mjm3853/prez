"""Template utilities for presentations."""

from enum import Enum
from pathlib import Path
from typing import Any


class SlideType(Enum):
    """Enum for different slide types."""
    TITLE = "title"
    CONTENT = "content"
    IMAGE = "image"
    COMPARISON = "comparison"
    SECTION = "section"


class SlideTemplate:
    """Template for creating slides with predefined structures."""

    def __init__(self, slide_type: SlideType, **kwargs: Any):
        """Initialize a slide template.

        Args:
            slide_type: Type of slide to create
            **kwargs: Additional template parameters
        """
        self.slide_type = slide_type
        self.params = kwargs

    @classmethod
    def title_slide(cls, title: str, subtitle: str = "") -> "SlideTemplate":
        """Create a title slide template."""
        return cls(SlideType.TITLE, title=title, subtitle=subtitle)

    @classmethod
    def content_slide(cls, title: str, content: list[str]) -> "SlideTemplate":
        """Create a content slide template."""
        return cls(SlideType.CONTENT, title=title, content=content)

    @classmethod
    def image_slide(cls, title: str, image_path: Path,
                   caption: str = "") -> "SlideTemplate":
        """Create an image slide template."""
        return cls(SlideType.IMAGE, title=title, image_path=image_path, caption=caption)

    @classmethod
    def section_slide(cls, title: str, description: str = "") -> "SlideTemplate":
        """Create a section divider slide template."""
        return cls(SlideType.SECTION, title=title, description=description)

    def to_dict(self) -> dict[str, Any]:
        """Convert template to dictionary."""
        return {
            "type": self.slide_type.value,
            "params": self.params
        }


class PresentationTemplate:
    """Template for entire presentations."""

    def __init__(self, name: str, slides: list[SlideTemplate] | None = None):
        """Initialize presentation template.

        Args:
            name: Template name
            slides: List of slide templates
        """
        self.name = name
        self.slides = slides or []

    def add_slide(self, slide_template: SlideTemplate) -> None:
        """Add a slide template to the presentation."""
        self.slides.append(slide_template)

    def to_dict(self) -> dict[str, Any]:
        """Convert presentation template to dictionary."""
        return {
            "name": self.name,
            "slides": [slide.to_dict() for slide in self.slides]
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PresentationTemplate":
        """Create presentation template from dictionary."""
        template = cls(data["name"])

        for slide_data in data.get("slides", []):
            slide_type = SlideType(slide_data["type"])
            slide_template = SlideTemplate(slide_type, **slide_data["params"])
            template.add_slide(slide_template)

        return template
