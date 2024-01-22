"""
File: run.py
Author: Steven "Kabbe" Karbjinsky
Description: Script to run the Spark Dash web application for analyzing GitLab repository data

For more information, see: https://github.com/xKabbe/spark
"""
from app.frontend.dashboard import app

if __name__ == '__main__':
    app.run_server(debug=True)
