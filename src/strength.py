def classify_strength(entropy):
    if entropy < 30:
        return "Very Weak"
    elif entropy < 50:
        return "Weak"
    elif entropy < 70:
        return "Moderate"
    elif entropy < 90:
        return "Strong"
    else:
        return "Very Strong"
