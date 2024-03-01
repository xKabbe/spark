"""
File: analysis.py
Author: Steven "Kabbe" Karbjinsky
Description: ...

For more information, see: https://github.com/xKabbe/spark
"""
# import os.path
# import time
# from os import stat_result

# from reportlab import pdfgen
# from rich import print
# from pathlib import Path
# from typing import Annotated

# import pandas as pd
# import typer
# from rich.progress import track, Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn, RenderableColumn, \
#     TotalFileSizeColumn, TaskProgressColumn
# from rich.tree import Tree

# from utils.report import Report
# from utils.file import File
# from decorators.progress_bar import progress_bar
# from decorators.spinner import spinner

# from reportlab.lib import colors
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen.canvas import Canvas

# app = typer.Typer()


# @spinner(duration=1)
# def prepare(path: str) -> None:
#     repository_path = Path(path)
#     if not repository_path.is_dir():
#         print('This is not a directory:', repository_path)
#         raise typer.Exit(code=1)


# # @progress_bar(duration=100)
# def analyse(path: str):
#     files = [File(name=file.stem,
#                   stats=file.stat(),
#                   extension=file.suffix[1:],
#                   parent_directory=file.parent)
#              for file in Path(path).rglob('*') if file.is_file()]
#     analysied_files = [file.to_dict() for file in files]

#     df = pd.DataFrame(data=analysied_files)
#     print(df.head())


# def get_dir_size(path):
#     size = 0
#     for file in Path(path).iterdir():
#         if file.is_file():
#             size += file.stat().st_size

#         if file.is_dir():
#             size += get_dir_size(file)

#     return size


# # python insight.py --path /path/to/git/repository --stats --file-types --contributors --complexity
# @app.command()
# def main(path: Annotated[str, typer.Option(help='Repository to be analysed')] = '../example_repository') -> None:
#     # with Progress(SpinnerColumn(),
#     #               TimeElapsedColumn(),
#     #               TextColumn("[progress.description]{task.description}")) as progress:
#     #     progress.add_task(description="Preparing...", total=None)
#     #     time.sleep(2)
#     # print("Done!")
#     #
#     # with Progress(SpinnerColumn(),
#     #               TimeElapsedColumn(),
#     #               TextColumn("[progress.description]{task.description}")) as progress:
#     #     progress.add_task(description="Processing...", total=None)
#     #     time.sleep(2)
#     # print("Done!")
#     #
#     # with Progress(BarColumn(),
#     #               TimeElapsedColumn(),
#     #               TextColumn("[progress.description]{task.description}")) as progress:
#     #     progress.add_task(description="Cleaning...", total=None)
#     #     time.sleep(2)
#     # print("Done!")

#     prepare(path=path)

#     size = get_dir_size(path)
#     size_in_mb = size / (1024 * 1024)
#     print(f"Total size of directory '{path}': {size:.2f} Bytes ({size_in_mb:.2f} MB)")

#     with Progress(TextColumn("[progress.description]{task.description}"),
#                   BarColumn(),
#                   TaskProgressColumn(),
#                   TimeElapsedColumn(),
#                   TotalFileSizeColumn()) as progress:
#         task_analysing = progress.add_task("[red]Analysing...", total=size)
#         task_reporting = progress.add_task("[green]Reporting...", total=size)

#         analysed_files = []

#         for file in Path(path).rglob('*'):
#             if file.is_file():
#                 analysed_file = File(name=file.stem,
#                                      stats=file.stat(),
#                                      extension=file.suffix[1:],
#                                      parent_directory=file.parent)

#                 analysed_files.append(analysed_file.to_dict())
#                 progress.update(task_analysing, advance=file.stat().st_size)
#                 time.sleep(0.01)

#         pdf_report = Report(file_path='../out/code_insight_report.pdf', title='Example Report')
#         # pdf_report.add_title(text='Example Report', position=(50, 700))
#         # pdf_report.add_title(text='Chapter 1', size=18, position=(50, 660))
#         # pdf_report.add_text(text='In this tutorial, we will demonstrate how to create PDF files using Python.',
#         #                     position=(50, 640))
#         # pdf_report.add_text(
#         #     text='Python is a versatile programming language that can be used to create different types of files, including PDFs.',
#         #     position=(50, 620))
#         # pdf_report.add_text(
#         #     text='By the end of this tutorial, you will be able to generate PDF files using Python and the ReportLab library.',
#         #     position=(50, 600))
#         # pdf_report.add_image(path=Path('../assets/go_logo.png'), position=(50, 400))
#         #
#         # pdf_report.close_page()
#         #
#         # pdf_report.add_title(text='Example Report', position=(50, 700))
#         # pdf_report.add_title(text='Chapter 2', size=18, position=(50, 660))

#         for file in analysed_files:
#             position = 700

#             pdf_report.add_title(text=file['name'], position=(50, 700))
#             pdf_report.add_text(text=f"Extension: {file['extension']}", position=(50, 685))
#             pdf_report.add_text(text=f"Size: {file['size']}", position=(50, 670))
#             pdf_report.add_text(text=f"Creation Time: {file['creation_time']}", position=(50, 655))
#             pdf_report.add_text(text=f"Modification Time: {file['modification_time']}", position=(50, 640))
#             pdf_report.add_text(text=f"Parent Directory: {file['parent_directory']}", position=(50, 625))

#             content_position = 610
#             for i, content_line in enumerate(file['content'][:5]):
#                 if i == 0:
#                     pdf_report.add_text(text=f"Content: {content_line[:50]}", position=(50, content_position))
#                 else:
#                     pdf_report.add_text(text=f"{content_line[:50]}", position=(107, content_position))
#                 content_position -= 15

#             pdf_report.add_text(text=f"Lines of Content: {file['lines_of_content']}", position=(50, 535))
#             pdf_report.add_text(text=f"Characters of Content: {file['characters_of_content']}", position=(50, 520))
#             pdf_report.close_page()

#             progress.update(task_reporting, advance=file['size'])
#             time.sleep(0.01)

#         pdf_report.create_report()

#         df = pd.DataFrame(data=analysed_files)
#         print(df.head())


# if __name__ == '__main__':
#     app()
