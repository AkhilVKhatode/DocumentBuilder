Xfrom typing import List, Dict, Any

class Document:
    """The complex object being constructed"""
    def __init__(self):
        self.sections = []
    
    def add_section(self, section_type: str, content: Any):
        self.sections.append({"type": section_type, "content": content})
    
    def display(self):
        print("Document Structure:")
        for i, section in enumerate(self.sections, 1):
            print(f"{i}. [{section['type'].upper()}] {section['content']}")

class DocumentBuilder:
    """Abstract builder interface"""
    def __init__(self):
        self.document = Document()
    
    def add_title(self, text: str):
        pass
    
    def add_paragraph(self, text: str):
        pass
    
    def add_image(self, path: str):
        pass
    
    def add_table(self, data: List[List[str]]):
        pass
    
    def get_document(self) -> Document:
        return self.document

class ReportBuilder(DocumentBuilder):
    """Concrete builder for reports"""
    def add_title(self, text: str):
        self.document.add_section("Title", f"REPORT: {text.upper()}")
    
    def add_paragraph(self, text: str):
        self.document.add_section("Paragraph", text)
    
    def add_image(self, path: str):
        self.document.add_section("Image", f"Image from: {path}")
    
    def add_table(self, data: List[List[str]]):
        table_str = "\n".join([" | ".join(row) for row in data])
        self.document.add_section("Table", table_str)

class ArticleBuilder(DocumentBuilder):
    """Concrete builder for articles"""
    def add_title(self, text: str):
        self.document.add_section("Title", f"Article: {text}")
    
    def add_paragraph(self, text: str):
        self.document.add_section("Paragraph", f"{text}\n")
    
    def add_image(self, path: str):
        self.document.add_section("Image", f"[Illustration: {path}]")
    
    def add_table(self, data: List[List[str]]):
        self.document.add_section("Table", "Data table omitted in article format")

class Director:
    """Oversees the construction process"""
    def __init__(self, builder: DocumentBuilder):
        self.builder = builder
    
    def construct_simple_document(self, title: str, paragraphs: List[str]):
        self.builder.add_title(title)
        for para in paragraphs:
            self.builder.add_paragraph(para)
    
    def construct_complex_document(self, title: str, content: List[Dict]):
        self.builder.add_title(title)
        for item in content:
            if item["type"] == "paragraph":
                self.builder.add_paragraph(item["content"])
            elif item["type"] == "image":
                self.builder.add_image(item["content"])
            elif item["type"] == "table":
                self.builder.add_table(item["content"])

# Client code
if __name__ == "__main__":
    # Create a report
    report_builder = ReportBuilder()
    director = Director(report_builder)
    
    report_content = [
        {"type": "paragraph", "content": "This is the introduction."},
        {"type": "image", "content": "chart.png"},
        {"type": "table", "content": [["Name", "Age"], ["Alice", "30"], ["Bob", "25"]]},
        {"type": "paragraph", "content": "This is the conclusion."}
    ]
    
    director.construct_complex_document("Annual Report", report_content)
    report = report_builder.get_document()
    report.display()
    
    print("\n" + "="*50 + "\n")
    
    # Create an article
    article_builder = ArticleBuilder()
    director = Director(article_builder)
    
    director.construct_simple_document(
        "Python Design Patterns",
        [
            "The Builder pattern is useful for creating complex objects.",
            "It separates the construction from representation."
        ]
    )
    article = article_builder.get_document()
    article.display()
