def convert_case(text, case_type):
    """
    Converts a string to the specified case.

    case_type options:
    - 'upper' -> UPPERCASE
    - 'lower' -> lowercase
    - 'title' -> Title Case

    Returns an error message for invalid case types.
    """
    if case_type == "upper":
        return text.upper()
    elif case_type == "lower":
        return text.lower()
    elif case_type == "title":
        return text.title()
    else:
        return "Error: Invalid case_type. Use 'upper', 'lower', or 'title'."


# Test cases
print(convert_case("hello world", "upper"))
print(convert_case("HELLO WORLD", "lower"))
print(convert_case("python programming language", "title"))
print(convert_case("Hello World", "capitalize"))  # Invalid case type