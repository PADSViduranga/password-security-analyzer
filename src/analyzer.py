def analyze_password(password):
    result={
        "length": len(password),
        "has_uppercase": any(char.isupper() for char in password),
        "has_lowercase": any(char.islower() for char in password),
        "has_digit": any(char.isdigit() for char in password),
        "has_special": any(not char.isalnum() for char in password)
        }
    return result
