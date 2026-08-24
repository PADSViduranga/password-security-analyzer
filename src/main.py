
from entropy import calculate_characrer_pool, calculate_entropy

def main():
    pool = calculate_characrer_pool(password)
    entropy = calculate_entropy(password)

    print(f"\nCharacter Pool Size: {pool}")
    print(f"Estimated Entropy: {entropy:.2f} bits")

if __name__ == "__main__":
    main()

