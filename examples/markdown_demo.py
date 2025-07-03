#!/usr/bin/env python3
"""Demo script for markdown-based presentation creation."""

from pathlib import Path

from prez.core import PresentationBuilder


def main():
    """Run the markdown demo."""
    print("Prez Markdown Demo")
    print("==================")

    # Path to the sample markdown file
    sample_md = Path(__file__).parent / "sample_presentation.md"

    if not sample_md.exists():
        print(f"Error: Sample markdown file not found: {sample_md}")
        return

    print(f"Creating presentation from: {sample_md.name}")

    try:
        # Create presentation from markdown
        builder = PresentationBuilder.from_markdown(sample_md)

        # Save the presentation
        output_path = Path("outputs/markdown_demo.pptx")
        builder.save(output_path)

        print(f"✅ Presentation created: {output_path}")
        print(f"📄 Total slides: {builder.get_slide_count()}")
        print("📝 Slide titles:")

        for i, title in enumerate(builder.get_slide_titles(), 1):
            print(f"   {i}. {title}")

        print("\n🎯 Next steps:")
        print(f"   - Open {output_path} in PowerPoint")
        print(f"   - Try editing {sample_md.name} and regenerating")
        print("   - Create your own markdown templates")

    except Exception as e:
        print(f"❌ Error creating presentation: {e}")
        print("Make sure you have installed dependencies with 'uv sync'")


if __name__ == "__main__":
    main()
