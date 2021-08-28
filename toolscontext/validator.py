#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module Name

    Description...
"""

__version__ = "0.0.1"

import sys
import os 
import re
import unicodedata
from enum import Enum, auto

import PyQt5.QtWidgets as qtw
from enforce_typing import enforce_types

sys.path.insert(0, os.getcwd())
from models.toolscontext import customlogger


logger = customlogger.custom_logger(log_title="VALIDATOR ",file_handler=True,file_output="logs/validator.log")


class CaseStyle(Enum):
    Title = auto(),
    Capitalize = auto(),
    Upper = auto(),
    Lower = auto()


@enforce_types
def check_string(text: str,
                 isempty: bool = True,
                 isspace: bool = True,
                 lowercase: bool = False,
                 uppercase: bool = False,
                 numbers: bool = False,
                 accented_letters: bool = False,
                 cedilla: bool = False,
                 isolated_accents: bool = False,
                 punctuations: bool = False,
                 special_chars: bool = False,
                 white_spaces: bool = False,
                 break_lines: bool = False,
                 non_unicode: bool = False) -> tuple[bool,str]:
    """
    Checks a string based on the parameters chosen by the user.

    Args:
        text (str): The string to be checked.
        isempty (bool): Checks if the string is empty. Defaults to True.
        isspace (bool): Checks if the string is only white spaces. Defaults to True.
        lowercase (bool): Checks if the string contains lowercases. Defaults to False.
        uppercase (bool): Checks if the string contains uppercases. Defaults to False.
        numbers (bool): Checks if the string contains numbers. Defaults to False.
        accented_letters (bool): Checks if the string contains accented letters. Defaults to False.
        cedilla (bool): Checks if the string contains cedilla. Defaults to False.
        isolated_accents (bool): Checks if the string contains isolated accents. Defaults to False.
            "`´^~¨"
        punctuations (bool): Checks if the string contains punctuations. Defaults to False.
            ".:,;\-_<>=+*!?)(}{|''""\][\\/"
        special_chars (bool): Checks if the string contains special characters. Defaults to False.
            "@#$%&"
        white_spaces (bool): Checks if the string contains white spaces. Defaults to False.
        break_lines (bool): Checks if the string contains break lines. Defaults to False.
        non_unicode (bool): Checks if the string contains non-unicode characters. Defaults to False.
        print_cmd (bool): Prints the alerts to the console. Defaults to False.

    Returns:
        True if the string passes all the tests, False if it fails at any.
    """
    # Is Empty
    if isempty and not text:
        logger.info("The string is empty!".format(text))
        return "isempty"

    # Is Space
    if isspace and text.isspace():
        logger.info("The string only contains white spaces!".format(text))
        return "isspace"

    # Lowercase
    if lowercase and re.search('[a-z]', text):
        logger.info("The string '{}' contains lowercase letters!".format(text))
        return "lowercase"

    # Uppercase
    if uppercase and re.search('[A-Z]', text):
        logger.info("The string '{}' contains uppercase letters!".format(text))
        return "uppercase"

    # Numbers
    if numbers and re.search('[\d]', text):
        logger.info("The string '{}' contains numbers!".format(text))
        return "numbers"

    # Accented letters
    if accented_letters and re.search('[àèìòùáéíóúâêîôûäëïöüãõ]', text):
        logger.info("The string '{}' contains accented letters!".format(text))
        return "accented_letters"

    # Cedilla
    if cedilla and re.search('[ç]', text):
        logger.info("The string '{}' contains cedilla!".format(text))
        return "cedilla"

    # Isolated Accents
    if isolated_accents and re.search('[`´^~¨]', text):
        logger.info("The string '{}' contains isolated accents!".format(text))
        return "isolated_accents"

    # Punctuations
    if punctuations and re.search('[.:,;\-_<>=+*!?)(}{|''""\][\\/]', text):
        logger.info("The string '{}' contains punctuations!".format(text))
        return "punctuations"

    # Special Characters
    if special_chars and re.search('[@#$%&]', text):
        logger.info("The string '{}' contains special characters!".format(text))
        return "special_chars"

    # Non-unicode
    if non_unicode and re.search('(?![ -~ç´¨àèìòùáéíóúâêîôûäëïöüãõ\n]).', text):
        logger.info("The string '{}' contains invalid characters!".format(text))
        return "non_unicode"

    # White Spaces
    if white_spaces and re.search('[\s]', text):
        logger.info("The string '{}' contains white spaces!".format(text))
        return "white_spaces"

    # Break Lines
    if break_lines and re.search('[\n]', text):
        logger.info("The string '{}' contains break lines!".format(text))
        return "break_lines"
        
    # Consider "¡" and "¿"?
    
    return False


@enforce_types
def format_string(text: str,
                  strip: bool = False, 
                  normalize: bool = False, 
                  case_style: CaseStyle = None) -> tuple[str, bool]:
    """
    Formats a string based on the parameters chosen by the user.

    Args:
        text (str): The string to be formatted.
        strip (bool): Strips the string. Defaults to False.
        normalize (bool): Removes all accents from the string. Defaults to False.
        case_style (stre.StrCase): Cases the string based on enum, which can be capitalize, title, uppercase or
            lowercase. Defaults to None.

    Returns:
        text (str): The formatted string.
        False if text isn't a string.
    """
    # Trims the string
    if strip:
        # text = " ".join(text.split())
        text = text.strip()

    # Normalizes the string
    if normalize:
        text = unicodedata.normalize('NFD', text).encode(
        'ascii', 'ignore').decode("utf-8")

    # Cases the string
    if case_style == CaseStyle.Capitalize:
        text = text.capitalize()
    elif case_style == CaseStyle.Title:
        text = text.title()
    elif case_style == CaseStyle.Upper:
        text = text.upper()
    elif case_style == CaseStyle.Lower:
        text = text.lower()

    return text
    

@enforce_types
def check_email() -> None:
    pass


@enforce_types
def check_int() -> None:
    pass


@enforce_types
def format_int() -> None:
    pass


@enforce_types
def check_float() -> None:
    pass


@enforce_types
def format_float() -> None:
    pass


@enforce_types
def check_binary() -> None:
    pass


@enforce_types
def format_binary() -> None:
    pass


@enforce_types
def check_date() -> None:
    pass


@enforce_types
def format_date() -> None:
    pass


@enforce_types
def check_currency() -> None:
    pass


@enforce_types
def format_currency() -> None:
    pass


if __name__ == "__main__":
    pass