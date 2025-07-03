"""Main entry point for the prez module."""

import sys
from pathlib import Path

from .core import PresentationBuilder


def main() -> None:
    """Main CLI entry point."""
    print("Prez - Presentation Builder")
    print("========================")

    if len(sys.argv) < 2:
        print("Usage: python -m prez <command>")
        print("Commands:")
        print("  demo - Run a demo presentation")
        print("  create <name> - Create a new presentation")
        print("  markdown <file.md> [output] - Create presentation from markdown")
        return

    command = sys.argv[1]

    if command == "demo":
        create_demo()
    elif command == "create" and len(sys.argv) > 2:
        create_presentation(sys.argv[2])
    elif command == "markdown" and len(sys.argv) > 2:
        markdown_file = sys.argv[2]
        output_name = sys.argv[3] if len(sys.argv) > 3 else None
        create_from_markdown(markdown_file, output_name)
    else:
        print(f"Unknown command: {command}")


def create_demo() -> None:
    """Create a demo presentation."""
    print("Creating demo presentation...")

    builder = PresentationBuilder()

    # Add title slide
    builder.add_title_slide(
        "Demo Presentation",
        "Built with Prez and python-pptx"
    )

    # Add content slides
    builder.add_content_slide(
        "Key Features",
        [
            "Python-powered presentation generation",
            "PowerPoint integration with python-pptx",
            "Template-based slide creation",
            "Programmatic content management"
        ]
    )

    builder.add_content_slide(
        "Getting Started",
        [
            "Install dependencies with 'uv sync'",
            "Run demo with 'moon run demo'",
            "Create custom presentations with the API",
            "Export to PowerPoint format"
        ]
    )

    # Save presentation
    output_path = Path("outputs/demo.pptx")
    builder.save(output_path)

    print(f"Demo presentation created: {output_path}")
    print(f"Slides created: {builder.get_slide_count()}")


def create_presentation(name: str) -> None:
    """Create a new presentation with the given name."""
    print(f"Creating presentation: {name}")

    builder = PresentationBuilder()
    builder.add_title_slide(name, "Created with Prez")

    output_path = Path(f"outputs/{name}.pptx")
    builder.save(output_path)

    print(f"Presentation created: {output_path}")


def create_from_markdown(markdown_file: str, output_name: str | None = None) -> None:
    """Create a presentation from a markdown template file."""
    markdown_path = Path(markdown_file)

    if not markdown_path.exists():
        print(f"Error: Markdown file not found: {markdown_file}")
        return

    print(f"Creating presentation from markdown: {markdown_file}")

    try:
        builder = PresentationBuilder.from_markdown(markdown_path)

        # Determine output name
        if output_name:
            output_path = Path(f"outputs/{output_name}.pptx")
        else:
            # Use markdown filename without extension
            output_path = Path(f"outputs/{markdown_path.stem}.pptx")

        builder.save(output_path)

        print(f"Presentation created: {output_path}")
        print(f"Slides created: {builder.get_slide_count()}")

    except Exception as e:
        print(f"Error creating presentation: {e}")


if __name__ == "__main__":
    main()
