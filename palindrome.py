def is_palindrome(s: str) -> bool:
    """Checks whether a string is a palindrome.

    Args:
        s (str): String to be checked.

    Returns:
        bool: Boolean indicating whether the given string is a palindrome.
    """
    return s == s[::-1]


if __name__ == "__main__":
    s1 = "124512512"
    # should return False
    print(is_palindrome(s1))

    s2 = "12321"
    # should return True
    print(is_palindrome(s2))
