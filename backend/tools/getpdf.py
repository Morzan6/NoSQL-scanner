from mdpdf.pdf_renderer import PdfRenderer
import commonmark

class ReportGenerator:
    def __init__(self) -> None:
        pass

    def convert(self, output_path: str, markdown: str) -> None:
        """Generate pdf file from markdown text.
        
        Args:
            output_path (str): absolute path to output pdf file.
            
            markdown (str): markdown text to be converted.
        """    
        parser = commonmark.Parser()
        renderer = PdfRenderer(output_path)
        ast = parser.parse(markdown)
        renderer.render(ast, markdown)
