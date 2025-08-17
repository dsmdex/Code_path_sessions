def one_char_palindrome(s: str) -> bool:
    """Return True if the string can be a palindrome by removing at most one char."""

    def is_palindrome_range(l: int, r: int) -> bool:
        """Check if s[l:r+1] is a palindrome."""
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Try removing either the left or the right character
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        left += 1
        right -= 1
    return True


print(one_char_palindrome("abca"))   # True  (remove 'b')
print(one_char_palindrome("abcca"))  # True  (remove one 'c')
print(one_char_palindrome("racecar")) # True (already palindrome)
print(one_char_palindrome("abcdef"))  # False
