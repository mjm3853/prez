"""Tests for the core presentation builder functionality."""

from prez.core import PresentationBuilder


class TestPresentationBuilder:
    """Test cases for PresentationBuilder class."""

    def test_initialization(self):
        """Test builder initialization."""
        builder = PresentationBuilder()
        assert builder.presentation is not None
        assert len(builder.slides) == 0

    def test_add_title_slide(self):
        """Test adding a title slide."""
        builder = PresentationBuilder()
        slide = builder.add_title_slide("Test Title", "Test Subtitle")

        assert slide is not None
        assert len(builder.slides) == 1
        assert builder.get_slide_count() == 1

    def test_add_content_slide(self):
        """Test adding a content slide."""
        builder = PresentationBuilder()
        content = ["Point 1", "Point 2", "Point 3"]
        slide = builder.add_content_slide("Test Content", content)

        assert slide is not None
        assert len(builder.slides) == 1
        assert builder.get_slide_count() == 1

    def test_get_slide_titles(self):
        """Test getting slide titles."""
        builder = PresentationBuilder()
        builder.add_title_slide("Title 1", "Subtitle 1")
        builder.add_content_slide("Title 2", ["Content"])

        titles = builder.get_slide_titles()
        assert len(titles) == 2
        assert "Title 1" in titles
        assert "Title 2" in titles

    def test_save_presentation(self, tmp_path):
        """Test saving presentation to file."""
        builder = PresentationBuilder()
        builder.add_title_slide("Test", "Test")

        output_path = tmp_path / "test.pptx"
        builder.save(output_path)

        assert output_path.exists()
        assert output_path.stat().st_size > 0

    def test_multiple_slides(self):
        """Test creating multiple slides."""
        builder = PresentationBuilder()

        builder.add_title_slide("Title", "Subtitle")
        builder.add_content_slide("Content 1", ["Item 1", "Item 2"])
        builder.add_content_slide("Content 2", ["Item 3", "Item 4"])

        assert builder.get_slide_count() == 3
        assert len(builder.slides) == 3

        titles = builder.get_slide_titles()
        assert "Title" in titles
        assert "Content 1" in titles
        assert "Content 2" in titles
