class Solution:
    def isPalindrome(self, s: str) -> bool:
        done = ''.join(i.lower() for i in s if i.isalnum())
        return done == done[::-1]