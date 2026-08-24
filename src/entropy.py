import math

def calculate_character_pool(password):
    pool = 0
    if any(char.islower() for char in password):
        pool += 26  # Lowercase letters
    if any(char.isupper() for char in password):
        pool += 26  # Uppercase letters
    if any(char.isdigit() for char in password):
        pool += 10  # Digits
    if any(not char.isalnum() for char in password):
        pool += 32  # Special characters (assuming standard ASCII special characters)
    return pool

def calculate_entropy(password):
    if not password:
        return 0
    pool = calculate_character_pool(password)
    return len(password) * math.log2(pool) if pool > 0 else 0
