"""BCSV file reading and writing.

This module provides a BCSV class that represents the file structure as a class. BCSV stands for Binary Comma Separated
Values, storing data in a table-like structure.


Typical usage example:
    with open("data.bcsv", "rb") as read_file:
        bcsv_obj = BCSV(read_file)

    with open("empty.bcsv", "wb") as write_file:
        bcsv_obj.write(write_file)
"""
from typing import BinaryIO, Literal

from src.tools.io import *

_byteorder: Literal["little", "big"] = "big"

class BCSVHeader:
    """Represents the BCSV file header as a class with I/O operations.
    """

    def __init__(self, file: BinaryIO | None = None) -> None:
        """Creates a new BCSVHeader instance.

        Args:
            file: If provided, initializes data using a file.
        """
        self.entry_count: UInt32 = 0x00000000
        self.field_count: UInt32 = 0x00000000
        self.data_section_offset: UInt32 = 0x00000000
        self.entry_size: UInt32 = 0x00000000

        # File initialization
        if file:
            self.read(file)

    def read(self, file: BinaryIO) -> None:
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

    def write(self, file: BinaryIO) -> None:
        """Write BCSV file data from this class.

        Args:
            file: The file to write to, opened in binary mode.
        """
        write_uint32(file, self.entry_count, _byteorder)
        write_uint32(file, self.field_count, _byteorder)
        write_uint32(file, self.data_section_offset, _byteorder)
        write_uint32(file, self.entry_size, _byteorder)

    def __str__(self) -> str:
        """Represents the BCSV header data as a human-readable string.

        Returns:
            A human-readable string containing object data.
        """
        return (f"Entry count: {self.entry_count}\n"
                + f"Field count: {self.field_count}\n"
                + f"Data section offset: {hex(self.data_section_offset)}\n"
                + f"Entry size: {self.entry_size} bytes")

    def __repr__(self) -> str:
        """Represents the BCSV header data as a string.

        Returns:
            A string containing object data.
        """
        return (f"{self.__class__.__name__}"
                + f"(entry_count={self.entry_count}, "
                + f"field_count={self.field_count}, "
                + f"data_section_offset={hex(self.data_section_offset)}, "
                + f"entry_size={hex(self.entry_size)})")

class BCSV:
    """Represents the BCSV file format as a class with i/o operations.
    """
    def __init__(self) -> None:
        """Creates a new BCSV instance.
        """
        self.header = BCSVHeader()
