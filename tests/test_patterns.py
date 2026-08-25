import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).parent.parent/"src"))

from patterns import detect_patterns

def test_common_password_pattern():
    warning = detect_patterns("password123")
    assert any("password" in warning.lower() for warning in warning)

def test_repeated_characters():
    warning = detect_patterns("aaa")
    assert any("repeated characters" in warning.lower() for warning in warning)

def test_number_sequence():
    warning = detect_patterns("123456")
    assert any("number sequence" in warning.lower() for warning in warning)

def test_letter_sequence():
    warning = detect_patterns("abcdef")
    assert any("letter sequence" in warning.lower() for warning in warning)

def test_no_obvious_patterns():
    warning = detect_patterns("vT7!qP2#xL9@rK4$")
    assert warning == []