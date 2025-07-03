"""Tests for markdown template functionality."""

from pathlib import Path
from textwrap import dedent

import pytest

from prez.markdown import MarkdownParser, create_presentation_from_markdown
from prez.templates import SlideType


class TestMarkdownParser:
    """Tests for MarkdownParser class."""

    def test_parse_simple_content_slides(self):
        """Test parsing simple content slides."""
        content = dedent("""
        # Introduction
        - First bullet point
        - Second bullet point

        ---

        # Getting Started
        - Install dependencies
        - Run the application
        """).strip()

        parser = MarkdownParser()
        template = parser.parse_content(content, "Test Presentation")

        assert template.name == "Test Presentation"
        assert len(template.slides) == 2

        # Check first slide
        slide1 = template.slides[0]
        assert slide1.slide_type == SlideType.CONTENT
        assert slide1.params['title'] == "Introduction"
        assert slide1.params['content'] == ["First bullet point", "Second bullet point"]

        # Check second slide
        slide2 = template.slides[1]
        assert slide2.slide_type == SlideType.CONTENT
        assert slide2.params['title'] == "Getting Started"
        assert slide2.params['content'] == ["Install dependencies", "Run the application"]

    def test_parse_with_frontmatter(self):
        """Test parsing markdown with YAML frontmatter."""
        content = dedent("""
        ---
        title: "My Presentation"
        author: "Test Author"
        ---

        # Welcome
        - This is the introduction
        """).strip()

        parser = MarkdownParser()
        template = parser.parse_content(content)

        assert template.name == "My Presentation"
        assert len(template.slides) == 1
        assert template.slides[0].params['title'] == "Welcome"

    def test_parse_title_slide(self):
        """Test parsing title slide with type directive."""
        content = dedent("""
        <!-- type: title -->
        # My Presentation
        A subtitle goes here
        """).strip()

        parser = MarkdownParser()
        template = parser.parse_content(content)

        assert len(template.slides) == 1
        slide = template.slides[0]
        assert slide.slide_type == SlideType.TITLE
        assert slide.params['title'] == "My Presentation"
        assert slide.params['subtitle'] == "A subtitle goes here"

    def test_parse_image_slide(self):
        """Test parsing image slide."""
        content = dedent("""
        <!-- type: image -->
        # Chart Results
        ![Chart showing growth](path/to/chart.png)
        This chart shows significant growth over time.
        """).strip()

        parser = MarkdownParser()
        template = parser.parse_content(content)

        assert len(template.slides) == 1
        slide = template.slides[0]
        assert slide.slide_type == SlideType.IMAGE
        assert slide.params['title'] == "Chart Results"
        assert slide.params['image_path'] == Path("path/to/chart.png")
        assert "This chart shows significant growth" in slide.params['caption']

    def test_parse_section_slide(self):
        """Test parsing section slide."""
        content = dedent("""
        <!-- type: section -->
        # Part Two
        Overview of advanced features
        """).strip()

        parser = MarkdownParser()
        template = parser.parse_content(content)

        assert len(template.slides) == 1
        slide = template.slides[0]
        assert slide.slide_type == SlideType.SECTION
        assert slide.params['title'] == "Part Two"
        assert slide.params['description'] == "Overview of advanced features"

    def test_parse_mixed_bullet_formats(self):
        """Test parsing different bullet point formats."""
        content = dedent("""
        # Mixed Bullets
        - Dash bullet
        * Asterisk bullet
        + Plus bullet
        Regular text line
        """).strip()

        parser = MarkdownParser()
        template = parser.parse_content(content)

        slide = template.slides[0]
        expected_content = [
            "Dash bullet",
            "Asterisk bullet",
            "Plus bullet",
            "Regular text line"
        ]
        assert slide.params['content'] == expected_content

    def test_parse_file_not_found(self, tmp_path):
        """Test parsing non-existent file raises error."""
        parser = MarkdownParser()
        non_existent = tmp_path / "missing.md"

        with pytest.raises(FileNotFoundError):
            parser.parse_file(non_existent)

    def test_parse_invalid_yaml_frontmatter(self):
        """Test handling invalid YAML frontmatter."""
        content = dedent("""
        ---
        invalid: yaml: content: here
        ---

        # Test Slide
        Content here
        """).strip()

        parser = MarkdownParser()

        with pytest.raises(ValueError, match="Invalid YAML frontmatter"):
            parser.parse_content(content)

    def test_parse_empty_slide_content(self):
        """Test handling empty slide content."""
        content = "---\n\n---\n\n# Valid Slide\n- Content here"

        parser = MarkdownParser()
        template = parser.parse_content(content)

        # Should skip empty slides
        assert len(template.slides) == 1
        assert template.slides[0].params['title'] == "Valid Slide"

    def test_create_presentation_from_markdown(self, tmp_path):
        """Test the convenience function for creating from markdown file."""
        markdown_file = tmp_path / "test.md"
        markdown_file.write_text(dedent("""
        ---
        title: "File Test"
        ---

        # Test Slide
        - Test content
        """).strip())

        template = create_presentation_from_markdown(markdown_file)

        assert template.name == "File Test"
        assert len(template.slides) == 1
        assert template.slides[0].params['title'] == "Test Slide"

    def test_parse_slide_without_title(self):
        """Test handling slide content without title returns None."""
        content = "Just some content without a title"

        parser = MarkdownParser()
        slide = parser._parse_slide(content)

        assert slide is None

    def test_parse_image_slide_simple_path(self):
        """Test parsing image slide with simple file path."""
        content = dedent("""
        <!-- type: image -->
        # Simple Image
        image.jpg
        Simple caption text
        """).strip()

        parser = MarkdownParser()
        template = parser.parse_content(content)

        slide = template.slides[0]
        assert slide.params['image_path'] == Path("image.jpg")
        assert slide.params['caption'] == "Simple caption text"
