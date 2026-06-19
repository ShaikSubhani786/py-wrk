def is_palindrome(text):
    """
    Returns True if the text is a palindrome,
    ignoring spaces and capitalization.
    """
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()

    # Check if the text reads the same forwards and backwards
    return cleaned_text == cleaned_text[::-1]


# Test cases
print(is_palindrome("racecar"))          # True
print(is_palindrome("RaceCar"))          # True
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))            # False
print(is_palindrome("Never odd or even")) # True