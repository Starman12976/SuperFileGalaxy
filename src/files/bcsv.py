"""BCSV file reading and writing.

This module provides a BCSV class that represents the file structure as a class. BCSV stands for Binary Comma Separated
Values, storing data in a table-like structure.

Typical usage example:

    TODO
"""
from typing import BinaryIO, Literal

from src.tools.io import *

_byteorder: Literal["little", "big"] = "big"

class BCSVHeader:
    """Represents the BCSV file header as a class with i/o operations.
    """

    def __init__(self: "BCSVHeader") -> None:
        """Creates a new BCSVHeader instance.
        """
        self.entry_count: UInt32 = 0x00000000
        self.field_count: UInt32 = 0x00000000
        self.data_section_offset: UInt32 = 0x00000000
        self.entry_size: UInt32 = 0x00000000

    def read(self: "BCSVHeader", file: BinaryIO) -> None:
        """Read BCSV file data into this class.

        Args:
            file: The file to read from, opened in binary mode.

        Raises:
            EOFError: If the file ends before all data can be read.
        """
        self.entry_count = read_uint32(file, _byteorder)
        self.field_count = read_uint32(file, _byteorder)
        self.data_section_offset = read_uint32(file, _byteorder)
        self.entry_size = read_uint32(file, _byteorder)

    def write(self: "BCSVHeader", file: BinaryIO) -> None:
        """Write BCSV file data from this class.

        Args:
            file: The file to write to, opened in binary mode.
        """


class BCSV:
    """Represents the BCSV file format as a class with i/o operations.
    """
