import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).parent.parent/"src"))

from entropy import calculate_character_pool,calculate_entropy

def test_lowercase_pool():
    pool = calculate_character_pool("abc")
    assert pool == 26

def test_uppercase_pool():
    pool = calculate_character_pool("ABC")
    assert pool == 26

def test_digit_pool():
    pool = calculate_character_pool("123")
    assert pool == 10

def test_special_character_pool():
    pool = calculate_character_pool("!@#")
    assert pool == 32

def test_mixed_character_pool():
    pool = calculate_character_pool("Hello123!")
    assert pool == 94

def test_empty_password_entropy():
    entropy = calculate_entropy("")
    assert entropy == 0

def test_entropy_is_positive():
    entropy = calculate_entropy("Hello123!")
    assert entropy > 0