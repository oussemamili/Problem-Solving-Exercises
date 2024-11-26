class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(letter for letter in s if letter.isalnum())
        return s.lower() == s[::-1].lower()