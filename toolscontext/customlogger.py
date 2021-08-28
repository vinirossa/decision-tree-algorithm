#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module Name

    Description...
"""

__version__ = "0.0.1"

import sys
import os
import logging
import traceback
import inspect
import datetime

from enforce_typing import enforce_types


FILE_FORMAT = ("%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s() - ln.%(lineno)d - %(message)s")


root_logger = logging.getLogger(__name__)
root_logger.setLevel(logging.INFO)
root_stream_handler = logging.StreamHandler(sys.stdout)
root_stream_handler.setLevel(logging.INFO)
root_formatter = logging.Formatter("ERROR HANDLER %(levelname)s: %(message)s")
root_stream_handler.setFormatter(root_formatter)
root_logger.addHandler(root_stream_handler)


@enforce_types
def custom_logger(log_level: int = logging.DEBUG,
                  log_title: str = "",
                  stream_handler: bool = True,
                  stream_level: int = logging.INFO,
                  stream_format: str = "%(levelname)s: %(message)s",
                  file_handler: bool = False,
                  file_level: int = logging.WARNING,
                  file_format: str = FILE_FORMAT,
                  file_output: str = "",
                  log_encoding: str = "utf-8") -> logging.Logger:

    caller = inspect.getmodule(inspect.stack()[2][0])
    
    logger = logging.getLogger(os.path.basename(caller.__file__))
    logger.setLevel(log_level)

    stream_formatter = logging.Formatter(log_title + stream_format)
    file_formatter = logging.Formatter(file_format)

    if stream_handler:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(stream_level)
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

    if file_handler:
        if file_output.strip():
            try:
                os.makedirs(os.path.abspath(os.path.dirname(file_output)),exist_ok=True)
                
            except OSError as e:
                root_logger.error("File output directory couldn't be created.")
                root_logger.exception(e)
                return False

            file_handler = logging.FileHandler(file_output,encoding=log_encoding)
            file_handler.setLevel(file_level)
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

        else:
            root_logger.error("If 'file_handler' is True, 'file_output' can't be empty.")
            return False

    return logger


@enforce_types
def console_logger(error):

    caller = inspect.getframeinfo(inspect.stack()[1][0])

    error_log = {"error_type": error.__class__.__name__,
                 "error_info": error.__doc__,
                 "error_file": os.path.basename(caller.filename),
                 "error_font": traceback.extract_tb(error.__traceback__,1)[0][2],
                 "error_line": error.__traceback__.tb_lineno,
                 "error_time": datetime.datetime.now(),
                 "error_details": str(error).capitalize()}
    
    print("----- ERROR -----")
    print("Type:",error_log["error_type"])
    print("Info:",error_log["error_info"])
    print("File:",error_log["error_file"])
    print("Font:",error_log["error_font"])
    print("Line:",error_log["error_line"])
    print("Time:",error_log["error_time"])
    print("Details:",error_log["error_details"])

    return error_log


@enforce_types
def sql_logger():
    pass


if __name__ == "__main__":
    pass