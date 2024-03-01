"""
File: progress_bar.py
Author: Steven "Kabbe" Karbjinsky
Description: ...

For more information, see: https://github.com/xKabbe/spark
"""
import functools
import time
from typing import Callable

from rich.progress import track


def progress_bar(duration: int) -> Callable:
    def decorator(func:Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total = 0
            result = func(*args, **kwargs)
            for value in track(range(duration), description='Analysing...'):
                time.sleep(0.01)
                total += 1

            print(f'Analysing complete')
            return result
        return wrapper
    return decorator
