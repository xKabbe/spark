"""
File: setup.py
Author: Steven "Kabbe" Karbjinsky
Description: Setup configuration for the Spark project

For more information, see: https://github.com/xKabbe/spark
"""
from setuptools import setup, find_packages

setup(
    name='spark',
    version='0.1.0',
    packages=find_packages(),
    python_requires='>=3.12',
    author='Steven Karbjinsky',
    author_email='steven.karbjinsky@web.de',
    description='A Python tool for analyzing GitLab repositories, providing insights into issue velocity, project milestones, and collaborative performance.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xKabbe/spark',
    keywords=[
        'gitlab',
        'repository',
        'data analysis',
        'project management',
        'issue tracking',
        'python',
        'data science'
    ],
    entry_points={
        'console_scripts': ['spark=app:run'],
    },
)

