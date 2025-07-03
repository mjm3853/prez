"""Tests for the template functionality."""

from pathlib import Path

from prez.templates import PresentationTemplate, SlideTemplate, SlideType


class TestSlideTemplate:
    """Test cases for SlideTemplate class."""

    def test_title_slide_template(self):
        """Test creating a title slide template."""
        template = SlideTemplate.title_slide("Test Title", "Test Subtitle")

        assert template.slide_type == SlideType.TITLE
        assert template.params["title"] == "Test Title"
        assert template.params["subtitle"] == "Test Subtitle"

    def test_content_slide_template(self):
        """Test creating a content slide template."""
        content = ["Point 1", "Point 2"]
        template = SlideTemplate.content_slide("Test Content", content)

        assert template.slide_type == SlideType.CONTENT
        assert template.params["title"] == "Test Content"
        assert template.params["content"] == content

    def test_image_slide_template(self):
        """Test creating an image slide template."""
        image_path = Path("test.jpg")
        template = SlideTemplate.image_slide("Test Image", image_path, "Caption")

        assert template.slide_type == SlideType.IMAGE
        assert template.params["title"] == "Test Image"
        assert template.params["image_path"] == image_path
        assert template.params["caption"] == "Caption"

    def test_section_slide_template(self):
        """Test creating a section slide template."""
        template = SlideTemplate.section_slide("Section Title", "Description")

        assert template.slide_type == SlideType.SECTION
        assert template.params["title"] == "Section Title"
        assert template.params["description"] == "Description"

    def test_template_to_dict(self):
        """Test converting template to dictionary."""
        template = SlideTemplate.title_slide("Test", "Subtitle")
        data = template.to_dict()

        assert data["type"] == "title"
        assert data["params"]["title"] == "Test"
        assert data["params"]["subtitle"] == "Subtitle"


class TestPresentationTemplate:
    """Test cases for PresentationTemplate class."""

    def test_initialization(self):
        """Test presentation template initialization."""
        template = PresentationTemplate("Test Template")

        assert template.name == "Test Template"
        assert len(template.slides) == 0

    def test_add_slide(self):
        """Test adding slides to presentation template."""
        template = PresentationTemplate("Test")
        slide = SlideTemplate.title_slide("Title", "Subtitle")

        template.add_slide(slide)

        assert len(template.slides) == 1
        assert template.slides[0] == slide

    def test_to_dict(self):
        """Test converting presentation template to dictionary."""
        template = PresentationTemplate("Test Template")
        slide = SlideTemplate.title_slide("Title", "Subtitle")
        template.add_slide(slide)

        data = template.to_dict()

        assert data["name"] == "Test Template"
        assert len(data["slides"]) == 1
        assert data["slides"][0]["type"] == "title"

    def test_from_dict(self):
        """Test creating presentation template from dictionary."""
        data = {
            "name": "Test Template",
            "slides": [
                {
                    "type": "title",
                    "params": {"title": "Test Title", "subtitle": "Test Subtitle"}
                }
            ]
        }

        template = PresentationTemplate.from_dict(data)

        assert template.name == "Test Template"
        assert len(template.slides) == 1
        assert template.slides[0].slide_type == SlideType.TITLE
        assert template.slides[0].params["title"] == "Test Title"
