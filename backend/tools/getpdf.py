from nmap.parser import parse_service
from nmap.markdown import to_markdown
from json import loads
from config import STATIC_FOLDER
from .ORM import Scan
import pypandoc as pd


class ReportGenerator:
    def __init__(self, scan: Scan) -> None:
        if not scan.vuln_data:
            raise ValueError("No vuln_data in the given scan")
        onejson = loads(scan.vuln_data)
        onejson["port"] = scan.port
        onejson["version"] = scan.version
        onejson["display_name"] = scan.type
        onejson["proto"] = "TCP"
        onejson["reason"] = ""
        self.markdown = to_markdown(parse_service(onejson))

        self.name = f"/{scan.id}-{scan.ip}.pdf"

        self.output_path = STATIC_FOLDER + self.name

    def convert(self) -> str:
        """Generate pdf file from markdown text.

        Args:
            output_path (str): absolute path to output pdf file.

            markdown (str): markdown text to be converted.
        """
        pd.ensure_pandoc_installed()
        pd.convert_text(
            f"# {self.name}\n\n" + self.markdown,
            "pdf",
            outputfile=STATIC_FOLDER + "self.name",
            format="md",
            extra_args=[
                "--pdf-engine=xelatex",
                "-V",
                "mainfont:CaskaydiaCove Nerd Font Propo",
                "-V",
                "block-headings",
                "-V",
                "'geometry:margin=1in'",
            ],
        )
        return self.output_path
