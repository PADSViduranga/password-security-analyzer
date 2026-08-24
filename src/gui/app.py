import tkinter as tk

import entropy
from .components import (
    create_header,
    create_password_input,
    create_analyze_button,
     create_results_area
)

from analyzer import analyze_password as analyze_password_data
from entropy import calculate_character_pool, calculate_entropy
from strength import classify_strength
from patterns import detect_patterns


class PasswordSecurityApp:
    def __init__(self):
        self.window = tk.Tk()



        self.window.title("Password Security Analyzer")
        self.window.geometry("700x600")
        self.window.resizable(False, False)

        create_header(self.window)
        self.password_entry = create_password_input(self.window)

        create_analyze_button(
            self.window, 
            self.analyze_password
            )

        self.results_label = create_results_area(self.window)


    def analyze_password(self):
        password= self.password_entry.get()

        analysis_result = analyze_password_data(password)
        pool = calculate_character_pool(password)
        entropy = calculate_entropy(password)
        strength = classify_strength(entropy)
        warnings = detect_patterns(password)

        result_text = (
            f"Length: {analysis_result['length']}\n"
            f"Uppercase: {analysis_result['has_uppercase']}\n"
            f"Lowercase: {analysis_result['has_lowercase']}\n"
            f"Digit: {analysis_result['has_digit']}\n"
            f"Special Character: {analysis_result['has_special']}"
            f"\nCharacter Pool Size: {pool}\n"
            f"Estimated Entropy: {entropy:.2f} bits\n"
            f"Password Strength: {strength}"
            f"\nSecurity Warnings:\n"
        )

        if warnings:
            result_text += "\n"
            for warning in warnings:
                result_text += f"- ⚠{warning}\n"

        else:
            result_text += "\n✓No security warnings detected."
        

        self.results_label.config(text=result_text)

        print(f"Analyzing password: {password}")
        print("analyzing passsword")
        print(f"Length: {analysis_result['length']}")
        print(f"Uppercase: {analysis_result['has_uppercase']}")
        print(f"Lowercase: {analysis_result['has_lowercase']}")
        print(f"Digit: {analysis_result['has_digit']}")
        print(f"Special Character: {analysis_result['has_special']}")



    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = PasswordSecurityApp()
    app.run()
