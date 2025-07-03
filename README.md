# Prez - Presentation Builder

A Python library for creating PowerPoint presentations programmatically using python-pptx, with modern Python tooling (uv) and task management (moonrepo).

## Features

- **Programmatic PowerPoint Generation**: Create presentations using Python code
- **Markdown Template Support**: Write presentations in markdown with YAML frontmatter
- **Template System**: Reusable slide templates for consistent formatting
- **Multiple Slide Types**: Title, content, section, and image slides
- **Modern Python Tooling**: Built with uv for dependency management
- **Task Management**: Moonrepo integration for streamlined development workflow
- **Extensible Architecture**: Easy to extend with custom slide types and layouts

## Quick Start

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- [moonrepo](https://moonrepo.dev/) (optional, for task management)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd prez

# Install dependencies
uv sync

# Run demo
uv run python examples/demo.py
```

### Basic Usage

```python
from pathlib import Path
from prez import PresentationBuilder

# Create a new presentation
builder = PresentationBuilder()

# Add slides
builder.add_title_slide("My Presentation", "Subtitle")
builder.add_content_slide("Key Points", [
    "Point 1",
    "Point 2", 
    "Point 3"
])

# Save presentation
builder.save(Path("my_presentation.pptx"))
```

### Creating from Markdown

```bash
# Create presentation from markdown template
uv run python -m prez markdown presentation.md

# With custom output name
uv run python -m prez markdown presentation.md my_slides
```

Example markdown template:
```markdown
---
title: "My Presentation"
author: "Your Name"
---

<!-- type: title -->
# Welcome
## Introduction to Prez

---

# Key Features
- Markdown-based authoring
- Automatic PowerPoint generation
- Multiple slide types
- YAML frontmatter support

---

<!-- type: section -->
# Getting Started
Let's dive into the basics

---

<!-- type: image -->
# Sample Chart
![Growth Chart](charts/growth.png)
This shows our progress over time.
```

### Using Templates

```python
from prez.templates import SlideTemplate, PresentationTemplate

# Create slide templates
title_slide = SlideTemplate.title_slide("Title", "Subtitle")
content_slide = SlideTemplate.content_slide("Content", ["Item 1", "Item 2"])

# Create presentation template
template = PresentationTemplate("My Template")
template.add_slide(title_slide)
template.add_slide(content_slide)
```

## Development

### Using uv (Recommended)

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Run linter
uv run ruff check

# Format code
uv run black .

# Type check
uv run mypy src

# Run demo
uv run python examples/demo.py

# Run CLI
uv run python -m prez demo
uv run python -m prez markdown examples/sample_presentation.md
```

### Using Moonrepo

```bash
# Install dependencies
moon run install

# Run development server
moon run dev

# Run tests
moon run test

# Run linter
moon run lint

# Format code
moon run format

# Type check
moon run typecheck

# Run demo
moon run demo
```

## Project Structure

```
prez/
├── src/prez/           # Main package
│   ├── __init__.py     # Package exports
│   ├── __main__.py     # CLI entry point
│   ├── core.py         # Core presentation builder
│   ├── markdown.py     # Markdown template parser
│   └── templates.py    # Template system
├── tests/              # Test suite
│   ├── test_core.py    # Core functionality tests
│   ├── test_markdown.py # Markdown parsing tests
│   └── test_templates.py # Template tests
├── examples/           # Example scripts
│   ├── demo.py         # Demo presentation
│   ├── markdown_demo.py # Markdown demo
│   └── sample_presentation.md # Sample markdown template
├── outputs/            # Generated presentations
├── .moon/              # Moonrepo configuration
│   └── workspace.yml   # Workspace settings
├── moon.yml            # Project configuration
├── pyproject.toml      # Python project configuration
└── README.md           # This file
```

## API Reference

### PresentationBuilder

Main class for building presentations:

- `add_title_slide(title, subtitle=None)` - Add a title slide
- `add_content_slide(title, content)` - Add a content slide with bullet points
- `add_image_slide(title, image_path, caption=None)` - Add a slide with an image
- `add_section_slide(title, description=None)` - Add a section divider slide
- `from_markdown(markdown_path, template_path=None)` - Create from markdown file
- `build_from_template(template)` - Build from presentation template
- `save(output_path)` - Save presentation to file
- `get_slide_count()` - Get number of slides
- `get_slide_titles()` - Get list of slide titles

### SlideTemplate

Template system for creating reusable slide layouts:

- `SlideTemplate.title_slide(title, subtitle)` - Create title slide template
- `SlideTemplate.content_slide(title, content)` - Create content slide template
- `SlideTemplate.image_slide(title, image_path, caption)` - Create image slide template
- `SlideTemplate.section_slide(title, description)` - Create section slide template

### MarkdownParser

Parse markdown files into presentation templates:

- `parse_file(markdown_path)` - Parse markdown file into presentation template
- `parse_content(content, name)` - Parse markdown content string
- `create_presentation_from_markdown(markdown_path)` - Convenience function

### CLI Commands

- `python -m prez demo` - Create demo presentation
- `python -m prez create <name>` - Create basic presentation
- `python -m prez markdown <file.md> [output]` - Create from markdown template

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `uv run pytest`
5. Run linter: `uv run ruff check`
6. Format code: `uv run black .`
7. Submit a pull request

## License

[Add your license here]
