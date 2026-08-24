import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from recommendations import generate_recommendations


def test_short_password_recommendation():
    analysis = {
        "length": 5,
        "has_uppercase": True,
        "has_lowercase": True,
        "has_digit": True,
        "has_special": True
    }

    recommendations = generate_recommendations(
        "Abc12",
        analysis,
        [],
        40
    )

    assert any("8 characters" in r for r in recommendations)


def test_missing_uppercase_recommendation():
    analysis = {
        "length": 10,
        "has_uppercase": False,
        "has_lowercase": True,
        "has_digit": True,
        "has_special": True
    }

    recommendations = generate_recommendations(
        "abc123!@#",
        analysis,
        [],
        55
    )

    assert any("uppercase" in r.lower() for r in recommendations)


def test_missing_lowercase_recommendation():
    analysis = {
        "length": 10,
        "has_uppercase": True,
        "has_lowercase": False,
        "has_digit": True,
        "has_special": True
    }

    recommendations = generate_recommendations(
        "ABC123!@#",
        analysis,
        [],
        55
    )

    assert any("lowercase" in r.lower() for r in recommendations)


def test_missing_digit_recommendation():
    analysis = {
        "length": 10,
        "has_uppercase": True,
        "has_lowercase": True,
        "has_digit": False,
        "has_special": True
    }

    recommendations = generate_recommendations(
        "Abcdef!@#",
        analysis,
        [],
        55
    )

    assert any("digit" in r.lower() for r in recommendations)


def test_missing_special_character_recommendation():
    analysis = {
        "length": 10,
        "has_uppercase": True,
        "has_lowercase": True,
        "has_digit": True,
        "has_special": False
    }

    recommendations = generate_recommendations(
        "Abcdef1234",
        analysis,
        [],
        55
    )

    assert any("special" in r.lower() for r in recommendations)


def test_low_entropy_recommendation():
    analysis = {
        "length": 10,
        "has_uppercase": True,
        "has_lowercase": True,
        "has_digit": True,
        "has_special": True
    }

    recommendations = generate_recommendations(
        "Abc123!@#",
        analysis,
        [],
        40
    )

    assert any("entropy" in r.lower() for r in recommendations)


def test_pattern_warning_recommendation():
    analysis = {
        "length": 10,
        "has_uppercase": True,
        "has_lowercase": True,
        "has_digit": True,
        "has_special": True
    }

    warnings = ["Contains a predictable number sequence"]

    recommendations = generate_recommendations(
        "Password123",
        analysis,
        warnings,
        60
    )

    assert any("patterns" in r.lower() for r in recommendations)


def test_strong_password_recommendation():
    analysis = {
        "length": 20,
        "has_uppercase": True,
        "has_lowercase": True,
        "has_digit": True,
        "has_special": True
    }

    recommendations = generate_recommendations(
        "vT7!qP2#xL9@rK4$sN8",
        analysis,
        [],
        100
    )

    assert recommendations == [
        "Your password is strong and follows best practices."
    ]