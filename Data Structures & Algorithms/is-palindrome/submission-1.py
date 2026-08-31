class Solution:
    def isPalindrome(self, s: str) -> bool:
        abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        f = ''.join([a for a in s if a in abc])
        lower = f.lower()
        print(lower)
        return lower == lower[::-1] 