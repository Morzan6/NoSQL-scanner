from mdpdf.pdf_renderer import PdfRenderer
import commonmark
from config  import STATIC_FOLDER


from mdpdf.pdf_renderer import PdfRenderer
import commonmark
from nmap.parser import parse_service
from nmap.markdown import to_markdown
from tools.ORM import Scan
from json import loads


from .ORM import Scan

class ReportGenerator:
    def __init__(self, scan: Scan) -> None:
        if not scan.vuln_data:
            raise ValueError("No vuln_data in the given scan")
        onejson = loads(scan.vuln_data)
        onejson['port'] = scan.port
        onejson['version'] = scan.version
        onejson['display_name'] = scan.type
        onejson['proto'] = "TCP"
        onejson['reason'] = ""
        self.markdown = to_markdown(onejson)
        
        self.name = f"/{scan.id}-{scan.ip}.pdf"

        self.output_path = STATIC_FOLDER + self.name

    def convert(self) -> str:
        """Generate pdf file from markdown text.

        Args:
            output_path (str): absolute path to output pdf file.

            markdown (str): markdown text to be converted.
        """
        parser = commonmark.Parser()
        renderer = PdfRenderer(self.output_path)
        ast = parser.parse(self.markdown)
        renderer.render(ast, self.markdown)
        
        return self.output_path
    
