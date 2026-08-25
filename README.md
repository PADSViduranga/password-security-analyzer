# Password Security Analyzer

A Python-based desktop application that analyzes password security using
password characteristics, character pool size, estimated entropy,
predictable pattern detection, password strength classification, and
security recommendations.

## Overview

The Password Security Analyzer helps users understand the security
characteristics of a password instead of relying on a simple "strong" or
"weak" label.

The application analyzes multiple password properties and presents the
results through a graphical user interface built with Tkinter.

## Features

- Password length analysis
- Uppercase character detection
- Lowercase character detection
- Digit detection
- Special character detection
- Character pool calculation
- Password entropy estimation
- Password strength classification
- Predictable pattern detection
- Security warnings
- Password recommendations
- Show/Hide password functionality
- Empty password validation
- Minimum password length validation
- Color-coded security feedback
- Automated testing with pytest

## Technologies Used

- Python
- Tkinter
- pytest
- Git
- GitHub

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/PasswordSecurityAnalyzer.git
cd PasswordSecurityAnalyzer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

For Git Bash on Windows:

```bash
source .venv/Scripts/activate
```

For Command Prompt:

```cmd
.venv\Scripts\activate
```

## Running the Application

From the project root:

```bash
cd src
python -m gui.app
```

The Password Security Analyzer graphical interface will open.

## Running Tests

From the project root:

```bash
python -m pytest
```

## How It Works

The Password Security Analyzer evaluates a password using several security
characteristics instead of relying on a single strength check.

### 1. Password Analysis

The analyzer checks the basic characteristics of the password:

- Password length
- Uppercase letters
- Lowercase letters
- Digits
- Special characters

### 2. Character Pool

The application determines the number of possible characters that could have
been used based on the character types present in the password.

### 3. Entropy Estimation

Password entropy is estimated using the character pool size and password
length.

A higher entropy value generally indicates a larger number of possible
password combinations.

### 4. Strength Classification

The estimated entropy is used to classify the password into different
strength levels:

- Very Weak
- Weak
- Moderate
- Strong
- Very Strong

### 5. Pattern Detection

The application checks for predictable password patterns that could make a
password easier to guess.

Detected patterns are displayed as security warnings.

### 6. Recommendations

Based on the analysis results and detected patterns, the application provides
recommendations to help improve password security.

## Graphical User Interface

The application provides a Tkinter-based graphical interface with:

- Password input field
- Show/Hide password functionality
- Analyze Password button
- Password strength indicator
- Security warnings
- Password recommendations
- Color-coded security feedback
- Empty password validation
- Minimum password length validation

## Testing

The project uses `pytest` for automated testing of the core password security
functionality.

The test suite covers:

- Password characteristic analysis
- Character pool calculation
- Entropy calculation
- Password strength classification
- Predictable pattern detection
- Security recommendations

To run the complete test suite:

```bash
python -m pytest
```

## Project Structure

```text
PasswordSecurityAnalyzer/
│
├── src/
│   ├── analyzer.py
│   ├── entropy.py
│   ├── strength.py
│   ├── patterns.py
│   ├── recommendations.py
│   │
│   └── gui/
│       ├── app.py
│       ├── components.py
│       └── styles.py
│
├── tests/
│
└── README.md
```

## Future Improvements

Possible future improvements include:

- Password generation
- Password strength score visualization
- Additional predictable pattern detection
- Common-password database checking
- More detailed entropy analysis
- Exporting analysis results
- Improved accessibility
- Additional automated test coverage

## License

This project is developed for educational and software engineering purposes.