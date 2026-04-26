"""Tests the IO module.
"""

from io import BytesIO

import pytest

from src.tools.io import (
    read_int8, read_uint8,
    read_int16, read_uint16,
    read_int32, read_uint32,
    read_int64, read_uint64
)

# === Value reading tests ===
def test_uint8_read():
    data_min = BytesIO(b"\x00")
    data_mid = BytesIO(b"\x80")
    data_max = BytesIO(b"\xFF")

    assert read_uint8(data_min, "little") == 0x00
    assert read_uint8(data_mid, "little") == 0x80
    assert read_uint8(data_max, "little") == 0xFF

def test_uint16_read_le():
    data_min = BytesIO(b"\x00\x00")
    data_mid = BytesIO(b"\x00\x80")
    data_max = BytesIO(b"\xFF\xFF")

    assert read_uint16(data_min, "little") == 0x00_00
    assert read_uint16(data_mid, "little") == 0x80_00
    assert read_uint16(data_max, "little") == 0xFF_FF

def test_uint16_read_be():
    data_min = BytesIO(b"\x00\x00")
    data_mid = BytesIO(b"\x80\x00")
    data_max = BytesIO(b"\xFF\xFF")

    assert read_uint16(data_min, "big") == 0x00_00
    assert read_uint16(data_mid, "big") == 0x80_00
    assert read_uint16(data_max, "big") == 0xFF_FF

def test_uint32_read_le():
    data_min = BytesIO(b"\x00\x00\x00\x00")
    data_mid = BytesIO(b"\x00\x00\x00\x80")
    data_max = BytesIO(b"\xFF\xFF\xFF\xFF")

    assert read_uint32(data_min, "little") == 0x00_00_00_00
    assert read_uint32(data_mid, "little") == 0x80_00_00_00
    assert read_uint32(data_max, "little") == 0xFF_FF_FF_FF

def test_uint32_read_be():
    data_min = BytesIO(b"\x00\x00\x00\x00")
    data_mid = BytesIO(b"\x80\x00\x00\x00")
    data_max = BytesIO(b"\xFF\xFF\xFF\xFF")

    assert read_uint32(data_min, "big") == 0x00_00_00_00
    assert read_uint32(data_mid, "big") == 0x80_00_00_00
    assert read_uint32(data_max, "big") == 0xFF_FF_FF_FF

def test_uint64_read_le():
    data_min = BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00")
    data_mid = BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x80")
    data_max = BytesIO(b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF")

    assert read_uint64(data_min, "little") == 0x00_00_00_00_00_00_00_00
    assert read_uint64(data_mid, "little") == 0x80_00_00_00_00_00_00_00
    assert read_uint64(data_max, "little") == 0xFF_FF_FF_FF_FF_FF_FF_FF

def test_uint64_read_be():
    data_min = BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00")
    data_mid = BytesIO(b"\x80\x00\x00\x00\x00\x00\x00\x00")
    data_max = BytesIO(b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF")

    assert read_uint64(data_min, "big") == 0x00_00_00_00_00_00_00_00
    assert read_uint64(data_mid, "big") == 0x80_00_00_00_00_00_00_00
    assert read_uint64(data_max, "big") == 0xFF_FF_FF_FF_FF_FF_FF_FF

def test_int8_read():
    data_min = BytesIO(b"\x80")
    data_mid = BytesIO(b"\x00")
    data_max = BytesIO(b"\x7F")

    assert read_int8(data_min, "little") == -0x80
    assert read_int8(data_mid, "little") == 0x00
    assert read_int8(data_max, "little") == 0x7F

def test_int16_read_le():
    data_min = BytesIO(b"\x00\x80")
    data_mid = BytesIO(b"\x00\x00")
    data_max = BytesIO(b"\xFF\x7F")

    assert read_int16(data_min, "little") == -0x80_00
    assert read_int16(data_mid, "little") == 0x00_00
    assert read_int16(data_max, "little") == 0x7F_FF

def test_int16_read_be():
    data_min = BytesIO(b"\x80\x00")
    data_mid = BytesIO(b"\x00\x00")
    data_max = BytesIO(b"\x7F\xFF")

    assert read_int16(data_min, "big") == -0x80_00
    assert read_int16(data_mid, "big") == 0x00_00
    assert read_int16(data_max, "big") == 0x7F_FF

def test_int32_read_le():
    data_min = BytesIO(b"\x00\x00\x00\x80")
    data_mid = BytesIO(b"\x00\x00\x00\x00")
    data_max = BytesIO(b"\xFF\xFF\xFF\x7F")

    assert read_int32(data_min, "little") == -0x80_00_00_00
    assert read_int32(data_mid, "little") == 0x00_00_00_00
    assert read_int32(data_max, "little") == 0x7F_FF_FF_FF

def test_int32_read_be():
    data_min = BytesIO(b"\x80\x00\x00\x00")
    data_mid = BytesIO(b"\x00\x00\x00\x00")
    data_max = BytesIO(b"\x7F\xFF\xFF\xFF")

    assert read_int32(data_min, "big") == -0x80_00_00_00
    assert read_int32(data_mid, "big") == 0x00_00_00_00
    assert read_int32(data_max, "big") == 0x7F_FF_FF_FF

def test_int64_read_le():
    data_min = BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x80")
    data_mid = BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00")
    data_max = BytesIO(b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x7F")

    assert read_int64(data_min, "little") == -0x80_00_00_00_00_00_00_00
    assert read_int64(data_mid, "little") == 0x00_00_00_00_00_00_00_00
    assert read_int64(data_max, "little") == 0x7F_FF_FF_FF_FF_FF_FF_FF

def test_int64_read_be():
    data_min = BytesIO(b"\x80\x00\x00\x00\x00\x00\x00\x00")
    data_mid = BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00")
    data_max = BytesIO(b"\x7F\xFF\xFF\xFF\xFF\xFF\xFF\xFF")

    assert read_int64(data_min, "big") == -0x80_00_00_00_00_00_00_00
    assert read_int64(data_mid, "big") == 0x00_00_00_00_00_00_00_00
    assert read_int64(data_max, "big") == 0x7F_FF_FF_FF_FF_FF_FF_FF

# === Endianness disagreement tests ===
def test_uint16_endianness_disagreement():
    data_mid: bytes = b"\x80\x00"

    assert read_uint16(BytesIO(data_mid), "little") == 0x00_80
    assert read_uint16(BytesIO(data_mid), "big") == 0x80_00

def test_uint32_endianness_disagreement():
    data_mid: bytes = b"\x80\x00\x00\x00"

    assert read_uint32(BytesIO(data_mid), "little") == 0x00_00_00_80
    assert read_uint32(BytesIO(data_mid), "big") == 0x80_00_00_00

def test_uint64_endianness_disagreement():
    data_mid: bytes = b"\x80\x00\x00\x00\x00\x00\x00\x00"

    assert read_uint64(BytesIO(data_mid), "little") == 0x00_00_00_00_00_00_00_80
    assert read_uint64(BytesIO(data_mid), "big") == 0x80_00_00_00_00_00_00_00

def test_int16_endianness_disagreement():
    data_max: bytes = b"\x7F\xFF"

    assert read_int16(BytesIO(data_max), "little") == -0x00_81
    assert read_int16(BytesIO(data_max), "big") == 0x7F_FF

def test_int32_endianness_disagreement():
    data_max: bytes = b"\x7F\xFF\xFF\xFF"

    assert read_int32(BytesIO(data_max), "little") == -0x00_00_00_81
    assert read_int32(BytesIO(data_max), "big") == 0x7F_FF_FF_FF

def test_int64_endianness_disagreement():
    data_max: bytes = b"\x7F\xFF\xFF\xFF\xFF\xFF\xFF\xFF"

    assert read_int64(BytesIO(data_max), "little") == -0x00_00_00_00_00_00_00_81
    assert read_int64(BytesIO(data_max), "big") == 0x7F_FF_FF_FF_FF_FF_FF_FF

# === Error paths ===
def test_8bit_int_error_paths():
    with pytest.raises(EOFError):
        read_uint8(BytesIO(b""), "little")
    with pytest.raises(EOFError):
        read_int8(BytesIO(b""), "big")

def test_16bit_int_error_paths():
    with pytest.raises(EOFError):
        read_uint16(BytesIO(b"\x00"), "little")
    with pytest.raises(EOFError):
        read_int16(BytesIO(b"\x00"), "big")

def test_32bit_int_error_paths():
    with pytest.raises(EOFError):
        read_uint32(BytesIO(b"\x00\x00\x00"), "little")
    with pytest.raises(EOFError):
        read_int32(BytesIO(b"\x00\x00\x00"), "big")

def test_64bit_int_error_paths():
    with pytest.raises(EOFError):
        read_uint64(BytesIO(b"\x00\x00\x00\x00\x00\x00\x00"), "little")
    with pytest.raises(EOFError):
        read_int64(BytesIO(b"\x00\x00\x00\x00\x00\x00\x00"), "big")

# === Multiple reads ===
def test_sequential_read():
    data = BytesIO(b"\x01" + b"\x02\x00" + b"\x03\x00\x00\x00" + b"\x04\x00\x00\x00\x00\x00\x00\x00")

    assert read_uint8(data, "little") == 1
    assert read_uint16(data, "little") == 2
    assert read_uint32(data, "little") == 3
    assert read_uint64(data, "little") == 4
    with pytest.raises(EOFError):
        read_uint8(data, "little")
