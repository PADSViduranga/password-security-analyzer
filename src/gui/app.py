import tkinter as tk
from .components import (
    create_header,
    create_password_input,
    create_analyze_button
)
from analyzer import analyze_password as analyze_password_data


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

    def analyze_password(self):
        password= self.password_entry.get()

        analysis_result = analyze_password_data(password)

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