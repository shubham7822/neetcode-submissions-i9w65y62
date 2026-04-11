class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left , right = 0, len(s) -1
        max_char =0
        charSet = set()
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            max_char = max(max_char, right - left + 1)
        return max_char
