import re

def is_strong_password(password):
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if not special_chars.search(password):
        return False

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return False

    consecutive_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(len(consecutive_chars) - 2):
        if consecutive_chars[i:i + 3] in password:
            return False

    keyboard_patterns = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "1234567890"]
    for pattern in keyboard_patterns:
        if pattern in password or pattern[::-1] in password:
            return False

    common_sequences = ["123", "234", "345", "abc", "bcd", "cde", "password", "qwerty"]
    for sequence in common_sequences:
        if sequence in password or sequence[::-1] in password:
            return False

    return True

def main():
    password = input("Enter your password: ")
    if is_strong_password(password):
        print("Your password is strong!")
    else:
        print("Your password is weak. Please use a stronger password.")


if __name__ == "__main__":
    main()
