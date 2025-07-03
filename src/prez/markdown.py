"""Markdown template parser for presentations."""

import re
from pathlib import Path
from typing import Any

import yaml

from .templates import PresentationTemplate, SlideTemplate, SlideType


class MarkdownParser:
    """Parser for markdown presentation templates."""

    def __init__(self) -> None:
        """Initialize the markdown parser."""
        self.frontmatter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
        self.slide_separator = re.compile(r'\n---\s*\n')

    def parse_file(self, markdown_path: Path) -> PresentationTemplate:
        """Parse a markdown file into a presentation template.

        Args:
            markdown_path: Path to the markdown file

        Returns:
            Parsed presentation template

        Raises:
            FileNotFoundError: If the markdown file doesn't exist
            ValueError: If the markdown format is invalid
        """
        if not markdown_path.exists():
            raise FileNotFoundError(f"Markdown file not found: {markdown_path}")

        content = markdown_path.read_text(encoding='utf-8')
        return self.parse_content(content, markdown_path.stem)

    def parse_content(self, content: str, name: str = "Untitled") -> PresentationTemplate:
        """Parse markdown content into a presentation template.

        Args:
            content: Markdown content string
            name: Name for the presentation

        Returns:
            Parsed presentation template
        """
        # Extract frontmatter if present
        metadata: dict[str, Any] = {}
        frontmatter_match = self.frontmatter_pattern.match(content)
        if frontmatter_match:
            try:
                metadata = yaml.safe_load(frontmatter_match.group(1)) or {}
                content = content[frontmatter_match.end():]
            except yaml.YAMLError as e:
                raise ValueError(f"Invalid YAML frontmatter: {e}") from e

        # Use title from metadata if available
        presentation_name = metadata.get('title', name)
        template = PresentationTemplate(presentation_name)

        # Split content into slides
        slide_contents = self.slide_separator.split(content.strip())

        for slide_content in slide_contents:
            if slide_content.strip():
                slide_template = self._parse_slide(slide_content.strip())
                if slide_template:
                    template.add_slide(slide_template)

        return template

    def _parse_slide(self, content: str) -> SlideTemplate | None:
        """Parse a single slide from markdown content.

        Args:
            content: Markdown content for the slide

        Returns:
            Parsed slide template or None if invalid
        """
        lines = content.split('\n')
        if not lines:
            return None

        # Check for slide type directive (e.g., <!-- type: image -->)
        slide_type = SlideType.CONTENT  # Default
        type_match = re.search(r'<!--\s*type:\s*(\w+)\s*-->', content)
        if type_match:
            try:
                slide_type = SlideType(type_match.group(1).lower())
                # Remove the directive from content
                content = re.sub(r'<!--\s*type:\s*\w+\s*-->\s*', '', content)
                lines = content.split('\n')
            except ValueError:
                pass  # Use default if invalid type

        # Extract title (first heading)
        title = ""
        content_lines = []
        title_found = False

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith('#') and not title_found:
                title = line.lstrip('#').strip()
                title_found = True
            elif title_found:
                content_lines.append(line)

        if not title:
            return None

        # Parse based on slide type
        if slide_type == SlideType.TITLE:
            subtitle = content_lines[0] if content_lines else ""
            return SlideTemplate.title_slide(title, subtitle)

        elif slide_type == SlideType.IMAGE:
            return self._parse_image_slide(title, content_lines)

        elif slide_type == SlideType.SECTION:
            description = '\n'.join(content_lines) if content_lines else ""
            return SlideTemplate.section_slide(title, description)

        else:  # Default to content slide
            bullet_points = []
            for line in content_lines:
                if line.startswith('- ') or line.startswith('* '):
                    bullet_points.append(line[2:].strip())
                elif line.startswith('+ '):
                    bullet_points.append(line[2:].strip())
                elif line and not line.startswith('#'):
                    bullet_points.append(line)

            return SlideTemplate.content_slide(title, bullet_points)

    def _parse_image_slide(self, title: str, content_lines: list[str]) -> SlideTemplate:
        """Parse an image slide from content lines.

        Args:
            title: Slide title
            content_lines: Content lines to parse

        Returns:
            Image slide template
        """
        image_path = Path("placeholder.jpg")  # Default
        caption_parts = []

        for line in content_lines:
            # Look for image markdown: ![alt](path)
            img_match = re.search(r'!\[([^\]]*)\]\(([^)]+)\)', line)
            if img_match:
                image_path = Path(img_match.group(2))
                alt_text = img_match.group(1)
                if alt_text:
                    caption_parts.append(alt_text)
            # Look for plain path
            elif line.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                image_path = Path(line)
            # Other lines become caption
            elif line and not line.startswith('!'):
                caption_parts.append(line)

        caption = '\n'.join(caption_parts) if caption_parts else ""
        return SlideTemplate.image_slide(title, image_path, caption)


def create_presentation_from_markdown(
    markdown_path: Path,
    template_path: Path | None = None
) -> PresentationTemplate:
    """Create a presentation template from a markdown file.

    Args:
        markdown_path: Path to the markdown template file
        template_path: Optional PowerPoint template file

    Returns:
        Presentation template ready for building
    """
    parser = MarkdownParser()
    return parser.parse_file(markdown_path)
