# Document Builder Design Pattern in Python

A Python implementation of the Builder design pattern for creating complex documents (reports, articles) with varying sections.

## Features

- Build documents step-by-step with different sections (titles, paragraphs, images, tables)
- Support for different document types (reports, articles) through concrete builders
- Clear separation between document construction and representation
- Optional Director class for standardized construction processes

## Usage
```
from builders import ReportBuilder, ArticleBuilder, Director

# Example 1: Building a report with Director
report_builder = ReportBuilder()
director = Director(report_builder)

content = [
    {"type": "paragraph", "content": "First paragraph"},
    {"type": "image", "content": "chart.png"},
    {"type": "table", "content": [["Data", "Value"], ["A", "1"]]}
]

director.construct_complex_document("My Report", content)
report = report_builder.get_document()
report.display()

# Example 2: Building directly with a builder
article_builder = ArticleBuilder()
article_builder.add_title("My Article")
article_builder.add_paragraph("Article content goes here")
article = article_builder.get_document()
article.display()
```
