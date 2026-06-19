def validate_password(password):
    errors = []
    special_chars = "!@#$%^&*"

    # Rule 1: Minimum length
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    # Rule 2: Uppercase letter
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")

    # Rule 3: Lowercase letter
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")

    # Rule 4: Digit
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit.")

    # Rule 5: Special character
    if not any(char in special_chars for char in password):
        errors.append(
            "Password must contain at least one special character (!@#$%^&*)."
        )

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }


# Test cases
print(validate_password("Password123!"))
print(validate_password("password"))
print(validate_password("PASSWORD123"))
print(validate_password("Pass12"))