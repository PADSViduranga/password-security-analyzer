import tkinter as tk

from .styles import (
    VERY_WEAK_COLOR,
    WEAK_COLOR,
    MODERATE_COLOR,
    STRONG_COLOR,
    VERY_STRONG_COLOR,
    WARNING_COLOR,
    RECOMMENDATION_COLOR,
    TEXT
)

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
from recommendations import generate_recommendations


class PasswordSecurityApp:

    def __init__(self):
        self.window = tk.Tk()

        self.window.title("Password Security Analyzer")
        self.window.geometry("700x850")
        self.window.resizable(False, False)

        create_header(self.window)

        self.password_entry = create_password_input(
            self.window
        )

        create_analyze_button(
            self.window,
            self.analyze_password
        )

        (
            self.results_label,
            self.strength_label,
            self.warnings_label,
            self.recommendations_label
        ) = create_results_area(self.window)

    def analyze_password(self):
        password = self.password_entry.get()

        # Analyze password characteristics
        analysis_result = analyze_password_data(password)

        # Calculate entropy
        pool = calculate_character_pool(password)
        entropy = calculate_entropy(password)

        # Determine strength
        strength = classify_strength(entropy)

        # Select strength color
        if strength == "Very Weak":
            strength_color = VERY_WEAK_COLOR

        elif strength == "Weak":
            strength_color = WEAK_COLOR

        elif strength == "Moderate":
            strength_color = MODERATE_COLOR

        elif strength == "Strong":
            strength_color = STRONG_COLOR

        elif strength == "Very Strong":
            strength_color = VERY_STRONG_COLOR

        else:
            strength_color = TEXT

        # Update strength
        self.strength_label.config(
            text=f"Strength: {strength}",
            fg=strength_color
        )

        # Detect patterns
        warnings = detect_patterns(password)

        # Generate recommendations
        recommendations = generate_recommendations(
            password,
            analysis_result,
            warnings,
            entropy
        )

        # General analysis results
        result_text = (
            f"Length: {analysis_result['length']}\n"
            f"Uppercase: {analysis_result['has_uppercase']}\n"
            f"Lowercase: {analysis_result['has_lowercase']}\n"
            f"Digit: {analysis_result['has_digit']}\n"
            f"Special Character: {analysis_result['has_special']}\n"
            f"Character Pool Size: {pool}\n"
            f"Estimated Entropy: {entropy:.2f} bits"
        )

        self.results_label.config(
            text=result_text
        )

        # Security warnings
        if warnings:
            warning_text = "Security Warnings:\n\n"

            for warning in warnings:
                warning_text += f"⚠ {warning}\n"

            self.warnings_label.config(
                text=warning_text,
                fg=WARNING_COLOR
            )

        else:
            self.warnings_label.config(
                text="Security Warnings:\n\n✓ No security warnings detected.",
                fg=STRONG_COLOR
            )

        # Recommendations
        recommendation_text = "Recommendations:\n\n"

        for recommendation in recommendations:
            recommendation_text += f"• {recommendation}\n"

        self.recommendations_label.config(
            text=recommendation_text,
            fg=RECOMMENDATION_COLOR
        )

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = PasswordSecurityApp()
    app.run()