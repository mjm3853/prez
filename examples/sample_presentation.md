---
title: "Prez: Markdown to PowerPoint"
author: "Presentation Builder"
date: "2024"
---

<!-- type: title -->
# Prez: Markdown to PowerPoint
## Create presentations from markdown templates

---

<!-- type: section -->
# Introduction
Getting started with markdown-based presentations

---

# Key Features
- Write presentations in markdown format
- Support for multiple slide types
- YAML frontmatter for metadata
- Automatic PowerPoint generation
- Template-based architecture

---

# Supported Slide Types
- **Title slides** - Main presentation title
- **Content slides** - Bullet points and text
- **Section slides** - Chapter/section dividers
- **Image slides** - Pictures with captions

---

<!-- type: section -->
# Getting Started
How to create your first presentation

---

# Installation
- Clone the repository
- Install dependencies with `uv sync`
- Run tests with `uv run pytest`
- Try the demo with `uv run python -m prez demo`

---

# Creating Presentations
- Write your content in markdown format
- Use `---` to separate slides
- Add type directives for special slides
- Include YAML frontmatter for metadata
- Generate with `uv run python -m prez markdown file.md`

---

# Markdown Syntax
- Use `# Heading` for slide titles
- Use `- item` for bullet points
- Use `<!-- type: title -->` for title slides
- Use `<!-- type: section -->` for section dividers
- Use `<!-- type: image -->` for image slides

---

<!-- type: image -->
# Sample Chart
![Growth Chart](charts/growth.png)
This chart shows the exponential growth in markdown adoption for presentations.

---

# Advanced Features
- Template inheritance from PowerPoint files
- Custom slide layouts and themes
- Programmatic content generation
- Integration with existing workflows

---

# Thank You
Questions and feedback welcome!

- GitHub: https://github.com/yourname/prez
- Documentation: Check the README.md
- Examples: See the examples/ directory