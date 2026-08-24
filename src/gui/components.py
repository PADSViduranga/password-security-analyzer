import tkinter as tk

def create_header(parent):
    header=tk.Label(
        parent, 
        text="Password Security Analyzer", 
        font=("Helvetica", 24, "bold")
        )

    header.pack(pady=20)
    return header

def create_password_input(parent):
    container=tk.Frame(parent)

    label=tk.Label(
        container, 
        text="Enter Password:", 
        font=("Helvetica", 14)
        )

    label.pack(anchor="w")

    entry=tk.Entry(
        container,
        width=45,
        show="*",
        font=("Helvetica", 14)
    )

    entry.pack(pady=(5,5))

    def toggle_password():
        if entry.cget("show") == "*":
            entry.config(show="")
            toggle_button.config(text="Hide")
        else:
            entry.config(show="*")
            toggle_button.config(text="Show")

    toggle_button=tk.Button(
        container,
        text="Show",
        command=toggle_password,
        font=("Helvetica", 12)
    )
    toggle_button.pack()

    container.pack(pady=10)

    return entry

def create_analyze_button(parent, command):
    button = tk.Button(
        parent,
        text="Analyze Password",
        font=("Helvetica", 12, "bold"),
        command=command
    )

    button.pack(pady=15)

    return button

def create_results_area(parent):
    results_frame=tk.Frame(parent)

    results_title=tk.Label(
        results_frame,
        text="Analysis Results:",
        font=("Helvetica", 16, "bold")
    )
    results_title.pack(pady=(10,5))

    results_label=tk.Label(
        results_frame,
        text="Enter a password and click Analyze Password.",
        font=("Helvetica", 11),
         justify="left"
    )

    results_label.pack()

    results_frame.pack(pady=10)

    return results_label