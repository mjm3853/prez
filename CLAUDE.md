# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Prez is a Python library for creating PowerPoint presentations programmatically using python-pptx. It features a modern Python development setup with uv for dependency management and moonrepo for task orchestration.

## Architecture

### Core Components

- **PresentationBuilder** (`src/prez/core.py`): Main class for building presentations with methods for adding different slide types
- **Template System** (`src/prez/templates.py`): Reusable slide templates and presentation templates with SlideTemplate and PresentationTemplate classes
- **Markdown Parser** (`src/prez/markdown.py`): Converts markdown files with YAML frontmatter to presentation templates
- **CLI Interface** (`src/prez/__main__.py`): Command-line interface for creating presentations and running demos

### Key Design Patterns

- **Builder Pattern**: PresentationBuilder uses method chaining for slide creation
- **Template Pattern**: SlideTemplate provides factory methods for different slide types
- **Enum-based Type Safety**: SlideType enum ensures type safety for slide categories

## Development Commands

### Primary (uv-based)
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
uv run python -m prez create <name>
uv run python -m prez markdown <file.md> [output]
```

### Task Management (moonrepo)
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

# Build package
moon run build
```

## Project Structure

```
src/prez/           # Main package
├── __init__.py     # Package exports (PresentationBuilder, SlideTemplate, MarkdownParser)
├── __main__.py     # CLI entry point with demo, create, and markdown commands
├── core.py         # PresentationBuilder class with slide creation methods
├── markdown.py     # MarkdownParser for converting markdown to presentations
└── templates.py    # Template classes (SlideTemplate, PresentationTemplate, SlideType)

tests/              # Test suite
├── test_core.py    # Tests for PresentationBuilder functionality
├── test_markdown.py # Tests for markdown parsing functionality
└── test_templates.py # Tests for template system

examples/           # Example scripts
├── demo.py         # Comprehensive demo showing all features
├── markdown_demo.py # Demo for markdown-based presentation creation
└── sample_presentation.md # Sample markdown template

outputs/            # Generated presentations (created automatically)
```

## Development Guidelines

### Code Style
- **Line Length**: 88 characters (Black standard)
- **Type Hints**: Required for all public methods (mypy strict mode)
- **Import Style**: Use absolute imports from prez package
- **Docstrings**: Google-style docstrings for all public methods

### Testing
- **Framework**: pytest with fixtures for file paths
- **Coverage**: Test all public methods and error conditions
- **Mocking**: Use tmp_path fixture for file operations
- **Structure**: One test class per main class

### Adding New Features

1. **New Slide Types**: Add to SlideType enum and implement in both PresentationBuilder and SlideTemplate
2. **New Templates**: Extend SlideTemplate with factory methods
3. **CLI Commands**: Add to `__main__.py` with appropriate argument parsing
4. **Testing**: Add corresponding tests in test files

## Common Development Tasks

### Creating New Slide Types
1. Add enum value to SlideType in `templates.py`
2. Add factory method to SlideTemplate class
3. Add implementation method to PresentationBuilder class
4. Add tests for both template and builder functionality

### Running Integration Tests
```bash
# Run demo and check output
uv run python examples/demo.py
ls outputs/  # Check generated files

# Test CLI
uv run python -m prez demo
uv run python -m prez create test_presentation
uv run python -m prez markdown examples/sample_presentation.md
```

## Markdown Templates

### Overview
Prez supports creating presentations from markdown files with YAML frontmatter. This allows for version-controlled, text-based presentation authoring with automatic PowerPoint generation.

### Markdown Format
```markdown
---
title: "Presentation Title"
author: "Author Name"
---

<!-- type: title -->
# Main Title
Subtitle text

---

# Content Slide
- Bullet point one
- Bullet point two
- Regular text line

---

<!-- type: section -->
# Section Divider
Description of the section

---

<!-- type: image -->
# Image Slide
![Alt text](path/to/image.png)
Caption text for the image
```

### Supported Slide Types
- **Title slides**: `<!-- type: title -->` - Main presentation title with subtitle
- **Content slides**: Default type with bullet points and text
- **Section slides**: `<!-- type: section -->` - Chapter/section dividers  
- **Image slides**: `<!-- type: image -->` - Images with captions

### CLI Usage
```bash
# Convert markdown to presentation
uv run python -m prez markdown presentation.md

# With custom output name
uv run python -m prez markdown presentation.md my_slides

# Run markdown demo
uv run python examples/markdown_demo.py
```

### Programmatic Usage
```python
from prez.core import PresentationBuilder
from prez.markdown import MarkdownParser

# Method 1: Using PresentationBuilder
builder = PresentationBuilder.from_markdown(Path("presentation.md"))
builder.save(Path("output.pptx"))

# Method 2: Using MarkdownParser directly
parser = MarkdownParser()
template = parser.parse_file(Path("presentation.md"))
builder = PresentationBuilder()
builder.build_from_template(template)
builder.save(Path("output.pptx"))
```

## Dependencies

- **Core**: python-pptx (PowerPoint manipulation), pyyaml (YAML parsing)
- **Development**: pytest, ruff, black, mypy
- **Python Version**: 3.12+ (uses modern type hints)
- **Package Manager**: uv (modern Python package management)
- **Task Runner**: moonrepo (monorepo task orchestration)

## Key Files

- `pyproject.toml`: Project configuration with tool settings for black, mypy, pytest, and ruff
- `.ruff.toml`: Ruff linting configuration
- `.moon/workspace.yml`: Moonrepo workspace configuration
- `moon.yml`: Project-specific moonrepo configuration

## Development Best Practices

- **Code Quality Workflow**: 
  - After adding any code, always run linting, fix any issues, then run unit testing and fix any issues
  - After adding code, linting, and testing, with all issues fixed, then update the readme.md and claude.md with details about the changes and any updated tasks to be run