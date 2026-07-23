class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed = []

        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                reversed.append(s[i].lower())

        original = []
        for char in s:
            if char.isalnum():
                original.append(char.lower())

        return original == reversed
