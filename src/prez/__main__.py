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
        return

    command = sys.argv[1]

    if command == "demo":
        create_demo()
    elif command == "create" and len(sys.argv) > 2:
        create_presentation(sys.argv[2])
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


if __name__ == "__main__":
    main()
