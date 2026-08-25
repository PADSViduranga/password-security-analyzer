import tkinter as tk

from .styles import (
    RESULT_BG,
    SECTION_FONT,
    TITLE_FONT,
    PRIMARY,
    SECONDARY,
    TEXT,
    WHITE,
    LABEL_FONT,
    BUTTON_FONT,
    WARNING_COLOR,
    STRONG_COLOR
)


def create_header(parent):
    header = tk.Label(
        parent,
        text="Password Security Analyzer",
        font=TITLE_FONT,
        bg=PRIMARY,
        fg=WHITE
    )

    header.pack(
        fill="x",
        pady=(0, 10),
        ipady=10
    )

    return header


def create_password_input(parent):
    container = tk.Frame(parent)

    label = tk.Label(
        container,
        text="Enter Password:",
        font=LABEL_FONT,
        fg=TEXT
    )

    label.pack(anchor="w")

    entry = tk.Entry(
        container,
        width=45,
        show="*",
        font=LABEL_FONT,
        bg=WHITE,
        fg=TEXT,
        relief="solid",
        bd=1
    )

    entry.pack(pady=(5, 5))

    def toggle_password():
        if entry.cget("show") == "*":
            entry.config(show="")
            toggle_button.config(text="Hide")
        else:
            entry.config(show="*")
            toggle_button.config(text="Show")

    toggle_button = tk.Button(
        container,
        text="Show",
        command=toggle_password,
        font=LABEL_FONT,
        bg=SECONDARY,
        fg=TEXT,
        relief="solid",
        padx=15,
        pady=5
    )

    toggle_button.pack()

    container.pack(pady=10)

    return entry


def create_analyze_button(parent, command):
    button = tk.Button(
        parent,
        text="Analyze Password",
        font=BUTTON_FONT,
        bg=PRIMARY,
        fg=WHITE,
        activebackground=PRIMARY,
        activeforeground=WHITE,
        relief="flat",
        padx=25,
        pady=8,
        command=command
    )

    button.pack(pady=15)

    return button


def create_results_area(parent):
    results_frame = tk.Frame(
        parent,
        bg=RESULT_BG,
        relief="solid",
        bd=1
    )

    results_title = tk.Label(
        results_frame,
        text="Analysis Results:",
        font=SECTION_FONT,
        bg=RESULT_BG,
        fg=TEXT
    )

    results_title.pack(pady=(10, 5))

    # Separate strength display
    strength_label = tk.Label(
        results_frame,
        text="Strength: --",
        font=("Helvetica", 14, "bold"),
        bg=RESULT_BG,
        fg=TEXT
    )

    strength_label.pack(pady=(5, 10))

    # General analysis results
    results_label = tk.Label(
        results_frame,
        text="Enter a password and click Analyze Password.",
        font=LABEL_FONT,
        bg=RESULT_BG,
        fg=TEXT,
        justify="left",
        anchor="w",
        wraplength=580
    )

    results_label.pack(
        pady=(5, 10),
        padx=20,
        anchor="w"
    )

    # Security warnings
    warnings_label = tk.Label(
        results_frame,
        text="",
        font=LABEL_FONT,
        bg=RESULT_BG,
        fg=WARNING_COLOR,
        justify="left",
        anchor="w",
        wraplength=580
    )

    warnings_label.pack(
        pady=(5, 10),
        padx=20,
        anchor="w"
    )

    results_frame.pack(
        pady=15,
        padx=40,
        ipadx=30,
        ipady=12,
        fill="x"
    )

    return results_label, strength_label, warnings_label