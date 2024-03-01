"""
File: report.py
Author: Steven "Kabbe" Karbjinsky
Description: ...

For more information, see: https://github.com/xKabbe/spark
"""
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas


class Report:
    def __init__(self, file_path, title):
        self.file_path = file_path
        self.title = title

        self.canvas = Canvas(file_path, pagesize=letter)
        self.canvas.setTitle(title=self.title)

    def add_title(self, text, position, color=colors.grey, font='Helvetica-Bold', size=24):
        self.canvas.setFillColor(aColor=color)
        self.canvas.setFont(psfontname=font, size=size)
        self.canvas.drawString(x=position[0], y=position[1], text=text)

    def add_text(self, text, position, color=colors.black, font='Helvetica', size=14):
        self.canvas.setFillColor(aColor=color)
        self.canvas.setFont(psfontname=font, size=size)
        self.canvas.drawString(x=position[0], y=position[1], text=text)

    def add_image(self, path, position, width=100, height=100):
        self.canvas.drawImage(image=path, x=position[0], y=position[1], width=width, height=height)

    def close_page(self):
        self.canvas.showPage()

    def create_report(self):
        self.canvas.save()
