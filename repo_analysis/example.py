import tempfile

from fpdf import FPDF
import cairosvg

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'My PDF Document', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_svg_image(self, path, width=None, height=None):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            # Convert SVG to PNG and save to temporary file
            cairosvg.svg2png(url=path, write_to=temp_file.name)

            # Add PNG image to PDF
            self.image(temp_file.name, x=self.get_x(), w=width, h=height)


if __name__ == '__main__':
    # Create instance of FPDF class
    pdf = PDF()

    # Add a page
    pdf.add_page()

    # Set title
    pdf.set_title("My First PDF")

    # Set font for the entire document
    pdf.set_font("Arial", size=12)

    # Add a chapter title
    pdf.chapter_title("Chapter 1 : Introduction")

    # Add some paragraphs
    pdf.chapter_body("This is a simple example of how to create a PDF document using PyFPDF.")

    # Add another chapter title
    pdf.chapter_title("Chapter 2 : Features")

    # Add some more paragraphs
    pdf.chapter_body("PyFPDF provides a simple way to create PDF documents with Python.")

    # Add SVG image
    pdf.add_svg_image("../assets/py_logo.svg", width=50, height=50)

    # Output the PDF to a file
    pdf.output("example.pdf")