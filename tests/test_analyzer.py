import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).parent.parent/"src"))

from analyzer import analyze_password

def test_password_length():
    result = analyze_password("Hello123!")
    assert result['length'] == 9

def test__uppercase_detection():
    result = analyze_password("Hello123!")
    assert result['has_uppercase'] == True

def test_lowercase_detection():
    result = analyze_password("Hello123!")
    assert result['has_lowercase'] == True

def test_digit_detection():
    result = analyze_password("Hello123!")
    assert result['has_digit'] == True

def test_special_character_detection():
    result = analyze_password("Hello123!")
    assert result['has_special'] == True
