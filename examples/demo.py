"""Demo script showing how to use the Prez presentation builder."""

from pathlib import Path

from prez import PresentationBuilder


def main():
    """Run the demo."""
    print("Running Prez Demo")
    print("================")

    # Create presentation builder
    builder = PresentationBuilder()

    # Add title slide
    builder.add_title_slide(
        "Prez Demo Presentation",
        "Programmatic PowerPoint Generation with Python"
    )

    # Add introduction slide
    builder.add_content_slide(
        "What is Prez?",
        [
            "A Python library for creating PowerPoint presentations",
            "Built on top of python-pptx",
            "Supports templates and programmatic content generation",
            "Integrates with modern Python tooling (uv, moonrepo)"
        ]
    )

    # Add features slide
    builder.add_content_slide(
        "Key Features",
        [
            "Simple API for slide creation",
            "Support for text, images, and layouts",
            "Template-based presentation generation",
            "Export to standard PowerPoint format",
            "Extensible architecture"
        ]
    )

    # Add usage example slide
    builder.add_content_slide(
        "Usage Example",
        [
            "from prez import PresentationBuilder",
            "builder = PresentationBuilder()",
            "builder.add_title_slide('My Presentation')",
            "builder.add_content_slide('Topics', ['Item 1', 'Item 2'])",
            "builder.save(Path('my_presentation.pptx'))"
        ]
    )

    # Add development workflow slide
    builder.add_content_slide(
        "Development Workflow",
        [
            "uv sync - Install dependencies",
            "moon run dev - Run development server",
            "moon run test - Run tests",
            "moon run lint - Check code quality",
            "moon run demo - Run this demo"
        ]
    )

    # Save the presentation
    output_path = Path("outputs/demo_presentation.pptx")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    builder.save(output_path)

    print(f"Demo presentation created: {output_path}")
    print(f"Total slides: {builder.get_slide_count()}")
    print(f"Slide titles: {', '.join(builder.get_slide_titles())}")


if __name__ == "__main__":
    main()
