"""
File: fpdf_report.py
Author: Steven "Kabbe" Karbjinsky
Description: ...

For more information, see: https://github.com/xKabbe/spark
"""
from fpdf import FPDF


class FPDFReport(FPDF):
    """
    Additional methods:
       - add_page()
       - set_title()
       - set_font()
       -
    """
    def __init__(self, file_path, title, global_font='Arial', global_size=12):
        super().__init__()
        self.file_path = file_path
        self.title = title

        self.set_title(title=self.title)
        self.set_font(family=global_font, size=global_size)

    def add_header(self):
        self.set_font()
        self.cell()

    def add_footer(self):
        self.set_y()
        self.set_font()
        self.cell()

    def add_chapter_title(self):
        self.set_font()
        self.cell()
        self.ln()

    def add_chapter_body(self):
        self.set_font()
        self.multi_cell()
        self.ln()

    def add_image(self, path, position, width=100, height=100):
        if path.endswith('.svg'):
            self._add_svg_image()

        if path.endswith('.png'):
            self._add_png_image()

    def _add_svg_image(self):
        pass

    def _add_png_image(self):
        pass

    def create_report(self):
        self.output(self.file_path)
