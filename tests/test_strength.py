import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).parent.parent/"src"))

from strength import classify_strength

def test_very_weak_password():
    assert classify_strength(20) == "Very Weak"

def test_weak_password():
    assert classify_strength(40) == "Weak"

def test_moderate_password():
    assert classify_strength(60) == "Moderate"

def test_strong_password():
    assert classify_strength(80) == "Strong"

def test_very_strong_password():
    assert classify_strength(100) == "Very Strong"

