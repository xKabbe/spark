"""
File: spinner.py
Author: Steven "Kabbe" Karbjinsky
Description: ...

For more information, see: https://github.com/xKabbe/spark
"""
import functools
import time
from typing import Callable

from rich.progress import Progress, SpinnerColumn, TextColumn


def spinner(duration: int) -> Callable:
    def decorator(func:Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with Progress(SpinnerColumn(),
                          TextColumn("[progress.description]{task.description}"),
                          transient=True) as progress:
                progress.add_task(description="Preparing...", total=None)

                result = func(*args, **kwargs)

                time.sleep(duration)
                print('Preparation complete')
                return result
        return wrapper
    return decorator
