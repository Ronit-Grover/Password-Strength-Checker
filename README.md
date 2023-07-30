# Password-Strength-Checker

This is a Python script that checks the strength of a given password. It follows a set of rules to determine whether the password is strong or weak based on various criteria. A strong password is essential for ensuring the security of your accounts and data.

Usage:

    Run the Python script in any Python environment.
    Enter the password you want to check when prompted.

Requirements:

    Python 3.x
    re (Regular Expression) module

Function:
The script defines a function called is_strong_password(password), which takes a string (password) as input and returns True if the password is strong and False otherwise.

Criteria for a Strong Password:

    The password must be at least 8 characters long.
    The password must contain at least one uppercase letter and one lowercase letter.
    The password must contain at least one digit (0-9).
    The password must contain at least one special character (e.g., @, #, $, %, etc.).
    The password cannot contain three consecutive characters from the same character class (e.g., 'aaa' or '123').
    The password cannot contain three consecutive characters from the same row on the keyboard or the same column on the numeric pad.

Common Sequences and Keyboard Patterns:
The script also checks for some common insecure password patterns and keyboard sequences (e.g., '123', 'abc', 'qwerty', etc.). If any of these patterns are found in the password (or their reverse), the password is considered weak.

Example:

    "MyP@ssw0rd" ➔ Strong password
    "abc123" ➔ Weak password (contains 'abc' sequence)
    "Qwerty123" ➔ Weak password (contains 'qwerty' sequence)
    "P@ssw0rd123" ➔ Weak password (contains '123' sequence)
