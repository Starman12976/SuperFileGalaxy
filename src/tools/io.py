"""Common I/O operations for all files.

This module provides helper functions for reading and writing file data. This includes signed/unsigned integer and float
values and strings.

Typical usage example:

    with open("data.bin", "rb") as f:
        version: UInt16 = read_uint16(f, 'little')
        size: UInt32 = read_uint32(f, 'little')
"""

from annotated_types import Ge, Le
from typing import Annotated, BinaryIO, Literal

# Public API
__all__ = [
    # === Types ===
    # Signed int types
    "Int8", "Int16", "Int32", "Int64",

    # Unsigned int types
    "UInt8", "UInt16", "UInt32", "UInt64",

    # === Functions ===
    # Signed int functions
    "read_int8", "read_int16", "read_int32", "read_int64",

    # Unsigned int functions
    "read_uint8", "read_uint16", "read_uint32", "read_uint64",
]

# Custom types for signed integer ranges
type Int8 = Annotated[int, Ge(-128), Le(127)]
type Int16 = Annotated[int, Ge(-32_768), Le(32_767)]
type Int32 = Annotated[int, Ge(-2_147_483_648), Le(2_147_483_647)]
type Int64 = Annotated[int, Ge(-9_223_372_036_854_775_808), Le(9_223_372_036_854_775_807)]

# Custom types for unsigned integer ranges
type UInt8 = Annotated[int, Ge(0), Le(255)]
type UInt16 = Annotated[int, Ge(0), Le(65_535)]
type UInt32 = Annotated[int, Ge(0), Le(4_294_967_295)]
type UInt64 = Annotated[int, Ge(0), Le(18_446_744_073_709_551_615)]

def _read_bytes(file: BinaryIO, count: int) -> bytes:
    """Read an exact number of bytes from a file.

    Args:
        file: The file to read from.
        count: The number of bytes to read.

    Returns:
        The bytes read.

    Raises:
        EOFError: If the end-of-file is reached before reading the requested number of bytes.
        ValueError: If the number of bytes is not a valid value.
    """
    # Size check
    if count <= 0:
        raise ValueError("Byte count cannot be less than 1.")

    data: bytes = file.read(count)

    # Size check
    if len(data) != count:
        raise EOFError(f"Expected {count} bytes, got {len(data)}")

    return data

def _read_int(file: BinaryIO, size: int, byteorder: Literal["little", "big"], signed: bool) -> int:
    """Read an integer of a given size from a file.

    Args:
        file: The file to read from.
        size: The number of bytes to read.
        byteorder: The endianness of the file. Use 'little' for little-endian and 'big' for big-endian.
        signed: Whether the value of the integer is signed.

    Returns:
        The integer read.

    Raises:
        EOFError: If the end-of-file is reached before reading the requested number of bytes.
        ValueError: If the number of bytes is not a valid or supported value.
    """
    # Size check
    if not 1 <= size <= 8:
        raise ValueError("Integer size can only be 1-8 bytes")

    data: bytes = _read_bytes(file, size)

    return int.from_bytes(data, byteorder=byteorder, signed=signed)

def read_int8(file: BinaryIO, byteorder: Literal["little", "big"]) -> Int8:
    """Read a signed 8-bit integer from a file.

    Args:
        file: The file to read from.
        byteorder: The endianness of the file. Use 'little' for little-endian and 'big' for big-endian.

    Returns:
        The value as a signed 8-bit integer.

    Raises:
        EOFError: If the end-of-file is reached before enough bytes are read.
    """
    return _read_int(file, 1, byteorder, signed=True)

def read_uint8(file: BinaryIO, byteorder: Literal["little", "big"]) -> UInt8:
    """Read an unsigned 8-bit integer from a file.

    Args:
        file: The file to read from.
        byteorder: The endianness of the file. Use 'little' for little-endian and 'big' for big-endian.

    Returns:
        The value as an unsigned 8-bit integer.

    Raises:
        EOFError: If the end-of-file is reached before enough bytes are read.
    """
    return _read_int(file, 1, byteorder, signed=False)

def read_int16(file: BinaryIO, byteorder: Literal["little", "big"]) -> Int16:
    """Read a signed 16-bit integer from a file.

    Args:
        file: The file to read from.
        byteorder: The endianness of the file. Use 'little' for little-endian and 'big' for big-endian.

    Returns:
        The value as a signed 16-bit integer.

    Raises:
        EOFError: If the end-of-file is reached before enough bytes are read.
    """
    return _read_int(file, 2, byteorder, signed=True)

def read_uint16(file: BinaryIO, byteorder: Literal["little", "big"]) -> UInt16:
    """Read an unsigned 16-bit integer from a file.

    Args:
        file: The file to read from.
        byteorder: The endianness of the file. Use 'little' for little-endian and 'big' for big-endian.

    Returns:
        The value as an unsigned 16-bit integer.

    Raises:
        EOFError: If the end-of-file is reached before enough bytes are read.
    """
    return _read_int(file, 2, byteorder, signed=False)

def read_int32(file: BinaryIO, byteorder: Literal["little", "big"]) -> Int32:
    """Read a signed 32-bit integer from a file.

    Args:
        file: The file to read from.
        byteorder: The endianness of the file. Use 'little' for little-endian and 'big' for big-endian.

    Returns:
        The value as a signed 32-bit integer.

    Raises:
        EOFError: If the end-of-file is reached before enough bytes are read.
    """
    return _read_int(file, 4, byteorder, signed=True)

def read_uint32(file: BinaryIO, byteorder: Literal["little", "big"]) -> UInt32:
    """Read an unsigned 32-bit integer from a file.

    Args:
        file: The file to read from.
        byteorder: The endianness of the file. Use 'little' for little-endian and 'big' for big-endian.

    Returns:
        The value as an unsigned 32-bit integer.

    Raises:
        EOFError: If the end-of-file is reached before enough bytes are read.
    """
    return _read_int(file, 4, byteorder, signed=False)

def read_int64(file: BinaryIO, byteorder: Literal["little", "big"]) -> Int64:
    """Read a signed 64-bit integer from a file.

    Args:
        file: The file to read from.
        byteorder: The endianness of the file. Use 'little' for little-endian and 'big' for big-endian.

    Returns:
        The value as a signed 64-bit integer.

    Raises:
        EOFError: If the end-of-file is reached before enough bytes are read.
    """
    return _read_int(file, 8, byteorder, signed=True)

def read_uint64(file: BinaryIO, byteorder: Literal["little", "big"]) -> UInt64:
    """Read an unsigned 64-bit integer from a file.

    Args:
        file: The file to read from.
        byteorder: The endianness of the file. Use 'little' for little-endian and 'big' for big-endian.

    Returns:
        The value as an unsigned 64-bit integer.

    Raises:
        EOFError: If the end-of-file is reached before enough bytes are read.
    """
    return _read_int(file, 8, byteorder, signed=False)
