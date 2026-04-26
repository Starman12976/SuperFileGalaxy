"""Tests the IO module.
"""
from io import BytesIO
import pytest

from src.tools.io import *


# === Int reading tests ===

def test_uint8_read():
    data_min = BytesIO(b"\x00")
    data_mid = BytesIO(b"\x80")
    data_max = BytesIO(b"\xFF")

    assert read_uint8(data_min, "little") == 0x00
    assert read_uint8(data_mid, "big")    == 0x80
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


# === Endianness disagreement read tests ===

def test_read_uint16_endianness_disagreement():
    data_mid: bytes = b"\x80\x00"

    assert read_uint16(BytesIO(data_mid), "little") == 0x00_80
    assert read_uint16(BytesIO(data_mid), "big") == 0x80_00

def test_read_uint32_endianness_disagreement():
    data_mid: bytes = b"\x80\x00\x00\x00"

    assert read_uint32(BytesIO(data_mid), "little") == 0x00_00_00_80
    assert read_uint32(BytesIO(data_mid), "big") == 0x80_00_00_00

def test_read_uint64_endianness_disagreement():
    data_mid: bytes = b"\x80\x00\x00\x00\x00\x00\x00\x00"

    assert read_uint64(BytesIO(data_mid), "little") == 0x00_00_00_00_00_00_00_80
    assert read_uint64(BytesIO(data_mid), "big") == 0x80_00_00_00_00_00_00_00

def test_read_int16_endianness_disagreement():
    data_max: bytes = b"\x7F\xFF"

    assert read_int16(BytesIO(data_max), "little") == -0x00_81
    assert read_int16(BytesIO(data_max), "big") == 0x7F_FF

def test_read_int32_endianness_disagreement():
    data_max: bytes = b"\x7F\xFF\xFF\xFF"

    assert read_int32(BytesIO(data_max), "little") == -0x00_00_00_81
    assert read_int32(BytesIO(data_max), "big") == 0x7F_FF_FF_FF

def test_read_int64_endianness_disagreement():
    data_max: bytes = b"\x7F\xFF\xFF\xFF\xFF\xFF\xFF\xFF"

    assert read_int64(BytesIO(data_max), "little") == -0x00_00_00_00_00_00_00_81
    assert read_int64(BytesIO(data_max), "big") == 0x7F_FF_FF_FF_FF_FF_FF_FF


# === Read error tests ===

def test_read_8bit_int_error_paths():
    with pytest.raises(EOFError):
        read_uint8(BytesIO(b""), "little")
    with pytest.raises(EOFError):
        read_int8(BytesIO(b""), "big")

def test_read_16bit_int_error_paths():
    with pytest.raises(EOFError):
        read_uint16(BytesIO(b"\x00"), "little")
    with pytest.raises(EOFError):
        read_int16(BytesIO(b"\x00"), "big")

def test_read_32bit_int_error_paths():
    with pytest.raises(EOFError):
        read_uint32(BytesIO(b"\x00\x00\x00"), "little")
    with pytest.raises(EOFError):
        read_int32(BytesIO(b"\x00\x00\x00"), "big")

def test_read_64bit_int_error_paths():
    with pytest.raises(EOFError):
        read_uint64(BytesIO(b"\x00\x00\x00\x00\x00\x00\x00"), "little")
    with pytest.raises(EOFError):
        read_int64(BytesIO(b"\x00\x00\x00\x00\x00\x00\x00"), "big")


# === Sequential read test ===

def test_sequential_read():
    data = BytesIO(b"\x01" + b"\x02\x00" + b"\x03\x00\x00\x00" + b"\x04\x00\x00\x00\x00\x00\x00\x00")

    assert read_uint8(data, "little") == 1
    assert read_uint16(data, "little") == 2
    assert read_uint32(data, "little") == 3
    assert read_uint64(data, "little") == 4
    with pytest.raises(EOFError):
        read_uint8(data, "little")


# === Signed int write tests ===

def test_int8_write() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_int8(data_min, -0x80, 'little')
    write_int8(data_mid, 0x00, 'little')
    write_int8(data_max, 0x7F, 'little')

    assert data_min.getvalue() == b"\x80"
    assert data_mid.getvalue() == b"\x00"
    assert data_max.getvalue() == b"\x7F"

def test_int16_write_le() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_int16(data_min, -0x80_00, 'little')
    write_int16(data_mid, 0x00_00, 'little')
    write_int16(data_max, 0x7F_FF, 'little')

    assert data_min.getvalue() == b"\x00\x80"
    assert data_mid.getvalue() == b"\x00\x00"
    assert data_max.getvalue() == b"\xFF\x7F"

def test_int16_write_be() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_int16(data_min, -0x80_00, 'big')
    write_int16(data_mid, 0x00_00, 'big')
    write_int16(data_max, 0x7F_FF, 'big')

    assert data_min.getvalue() == b"\x80\x00"
    assert data_mid.getvalue() == b"\x00\x00"
    assert data_max.getvalue() == b"\x7F\xFF"

def test_int32_write_le() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_int32(data_min, -0x80_00_00_00, 'little')
    write_int32(data_mid, 0x00_00_00_00, 'little')
    write_int32(data_max, 0x7F_FF_FF_FF, 'little')

    assert data_min.getvalue() == b"\x00\x00\x00\x80"
    assert data_mid.getvalue() == b"\x00\x00\x00\x00"
    assert data_max.getvalue() == b"\xFF\xFF\xFF\x7F"

def test_int32_write_be() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_int32(data_min, -0x80_00_00_00, 'big')
    write_int32(data_mid, 0x00_00_00_00, 'big')
    write_int32(data_max, 0x7F_FF_FF_FF, 'big')

    assert data_min.getvalue() == b"\x80\x00\x00\x00"
    assert data_mid.getvalue() == b"\x00\x00\x00\x00"
    assert data_max.getvalue() == b"\x7F\xFF\xFF\xFF"

def test_int64_write_le() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_int64(data_min, -0x80_00_00_00_00_00_00_00, 'little')
    write_int64(data_mid, 0x00_00_00_00_00_00_00_00, 'little')
    write_int64(data_max, 0x7F_FF_FF_FF_FF_FF_FF_FF, 'little')

    assert data_min.getvalue() == b"\x00\x00\x00\x00\x00\x00\x00\x80"
    assert data_mid.getvalue() == b"\x00\x00\x00\x00\x00\x00\x00\x00"
    assert data_max.getvalue() == b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x7F"

def test_int64_write_be() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_int64(data_min, -0x80_00_00_00_00_00_00_00, 'big')
    write_int64(data_mid, 0x00_00_00_00_00_00_00_00, 'big')
    write_int64(data_max, 0x7F_FF_FF_FF_FF_FF_FF_FF, 'big')

    assert data_min.getvalue() == b"\x80\x00\x00\x00\x00\x00\x00\x00"
    assert data_mid.getvalue() == b"\x00\x00\x00\x00\x00\x00\x00\x00"
    assert data_max.getvalue() == b"\x7F\xFF\xFF\xFF\xFF\xFF\xFF\xFF"


# === Unsigned int write tests ===

def test_uint8_write() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_uint8(data_min, 0x00, 'little')
    write_uint8(data_mid, 0x80, 'big')
    write_uint8(data_max, 0xFF, 'little')

    assert data_min.getvalue() == b"\x00"
    assert data_mid.getvalue() == b"\x80"
    assert data_max.getvalue() == b"\xFF"

def test_uint16_write_le() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_uint16(data_min, 0x00_00, 'little')
    write_uint16(data_mid, 0x80_00, 'little')
    write_uint16(data_max, 0xFF_FF, 'little')

    assert data_min.getvalue() == b"\x00\x00"
    assert data_mid.getvalue() == b"\x00\x80"
    assert data_max.getvalue() == b"\xFF\xFF"

def test_uint16_write_be() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_uint16(data_min, 0x00_00, 'big')
    write_uint16(data_mid, 0x80_00, 'big')
    write_uint16(data_max, 0xFF_FF, 'big')

    assert data_min.getvalue() == b"\x00\x00"
    assert data_mid.getvalue() == b"\x80\x00"
    assert data_max.getvalue() == b"\xFF\xFF"

def test_uint32_write_le() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_uint32(data_min, 0x00_00_00_00, 'little')
    write_uint32(data_mid, 0x80_00_00_00, 'little')
    write_uint32(data_max, 0xFF_FF_FF_FF, 'little')

    assert data_min.getvalue() == b"\x00\x00\x00\x00"
    assert data_mid.getvalue() == b"\x00\x00\x00\x80"
    assert data_max.getvalue() == b"\xFF\xFF\xFF\xFF"

def test_uint32_write_be() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_uint32(data_min, 0x00_00_00_00, 'big')
    write_uint32(data_mid, 0x80_00_00_00, 'big')
    write_uint32(data_max, 0xFF_FF_FF_FF, 'big')

    assert data_min.getvalue() == b"\x00\x00\x00\x00"
    assert data_mid.getvalue() == b"\x80\x00\x00\x00"
    assert data_max.getvalue() == b"\xFF\xFF\xFF\xFF"

def test_uint64_write_le() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_uint64(data_min, 0x00_00_00_00_00_00_00_00, 'little')
    write_uint64(data_mid, 0x80_00_00_00_00_00_00_00, 'little')
    write_uint64(data_max, 0xFF_FF_FF_FF_FF_FF_FF_FF, 'little')

    assert data_min.getvalue() == b"\x00\x00\x00\x00\x00\x00\x00\x00"
    assert data_mid.getvalue() == b"\x00\x00\x00\x00\x00\x00\x00\x80"
    assert data_max.getvalue() == b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"

def test_uint64_write_be() -> None:
    data_min = BytesIO()
    data_mid = BytesIO()
    data_max = BytesIO()

    write_uint64(data_min, 0x00_00_00_00_00_00_00_00, 'big')
    write_uint64(data_mid, 0x80_00_00_00_00_00_00_00, 'big')
    write_uint64(data_max, 0xFF_FF_FF_FF_FF_FF_FF_FF, 'big')

    assert data_min.getvalue() == b"\x00\x00\x00\x00\x00\x00\x00\x00"
    assert data_mid.getvalue() == b"\x80\x00\x00\x00\x00\x00\x00\x00"
    assert data_max.getvalue() == b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"


# === Write signed int endianness disagreement tests ===

def test_write_int16_endianness_disagreement():
    data_le = BytesIO()
    data_be = BytesIO()

    write_int16(data_le, -0x00_81,"little")
    write_int16(data_be, 0x7F_FF, "big")

    assert data_le.getvalue() == b"\x7F\xFF"
    assert data_be.getvalue() == b"\x7F\xFF"

def test_write_int32_endianness_disagreement():
    data_le = BytesIO()
    data_be = BytesIO()

    write_int32(data_le, -0x00_00_00_81,"little")
    write_int32(data_be, 0x7F_FF_FF_FF, "big")

    assert data_le.getvalue() == b"\x7F\xFF\xFF\xFF"
    assert data_be.getvalue() == b"\x7F\xFF\xFF\xFF"

def test_write_int64_endianness_disagreement():
    data_le = BytesIO()
    data_be = BytesIO()

    write_int64(data_le, -0x00_00_00_00_00_00_00_81,"little")
    write_int64(data_be, 0x7F_FF_FF_FF_FF_FF_FF_FF, "big")

    assert data_le.getvalue() == b"\x7F\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
    assert data_be.getvalue() == b"\x7F\xFF\xFF\xFF\xFF\xFF\xFF\xFF"


# === Write unsigned int endianness disagreement tests ===

def test_write_uint16_endianness_disagreement():
    data_le = BytesIO()
    data_be = BytesIO()

    write_uint16(data_le, 0x80_00,"little")
    write_uint16(data_be, 0x80_00, "big")

    assert data_le.getvalue() == b"\x00\x80"
    assert data_be.getvalue() == b"\x80\x00"

def test_write_uint32_endianness_disagreement():
    data_le = BytesIO()
    data_be = BytesIO()

    write_uint32(data_le, 0x80_00_00_00,"little")
    write_uint32(data_be, 0x80_00_00_00, "big")

    assert data_le.getvalue() == b"\x00\x00\x00\x80"
    assert data_be.getvalue() == b"\x80\x00\x00\x00"

def test_write_uint64_endianness_disagreement():
    data_le = BytesIO()
    data_be = BytesIO()

    write_uint64(data_le, 0x80_00_00_00_00_00_00_00,"little")
    write_uint64(data_be, 0x80_00_00_00_00_00_00_00, "big")

    assert data_le.getvalue() == b"\x00\x00\x00\x00\x00\x00\x00\x80"
    assert data_be.getvalue() == b"\x80\x00\x00\x00\x00\x00\x00\x00"


# Int write error tests

def test_write_8bit_int_error_paths():
    with pytest.raises(ValueError):
        write_int8(BytesIO(), 0x80, "little")
    with pytest.raises(ValueError):
        write_uint8(BytesIO(), 0x01_00, "big")

def test_write_16bit_int_error_paths():
    with pytest.raises(ValueError):
        write_int16(BytesIO(), 0x80_00, "little")
    with pytest.raises(ValueError):
        write_uint16(BytesIO(), 0x01_00_00, "big")

def test_write_32bit_int_error_paths():
    with pytest.raises(ValueError):
        write_int32(BytesIO(), 0x80_00_00_00, "little")
    with pytest.raises(ValueError):
        write_uint32(BytesIO(), 0x01_00_00_00_00, "big")

def test_write_64bit_int_error_paths():
    with pytest.raises(ValueError):
        write_int64(BytesIO(), 0x80_00_00_00_00_00_00_00, "little")
    with pytest.raises(ValueError):
        write_uint64(BytesIO(), 0x01_00_00_00_00_00_00_00_00, "big")

# === Sequential write test ===

def test_sequential_write():
    data = BytesIO()

    write_int8(data, 0x01, "big")
    write_int16(data, 0x00_02, "big")
    write_int32(data, 0x00_00_00_03, "big")
    write_int64(data, 0x00_00_00_00_00_00_00_04, "big")

    assert data.getvalue() == b"\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04"
