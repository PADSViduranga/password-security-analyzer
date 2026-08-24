from analyzer import analyze_password
from entropy import calculate_character_pool, calculate_entropy

def main():
    print("="*45)
    print("Welcome to the Password Analyzer!")
    print("="*45)

    password = input("Enter a password to analyze: ")
    analysis_result = analyze_password(password)
    
    print("\nPassword Analysis:")
    print(f"Length: {analysis_result['length']}")
    print(f"Contains Uppercase: {analysis_result['has_uppercase']}")
    print(f"Contains Lowercase: {analysis_result['has_lowercase']}")
    print(f"Contains Digit: {analysis_result['has_digit']}")
    print(f"Contains Special Character: {analysis_result['has_special']}")

    pool = calculate_character_pool(password)
    entropy = calculate_entropy(password)

    print(f"\nCharacter Pool Size: {pool}")
    print(f"Estimated Entropy: {entropy:.2f} bits")


if __name__ == "__main__":
    main()
