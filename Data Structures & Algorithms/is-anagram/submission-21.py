class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        charCount = [0] * 26

        for key , ch in enumerate(s):
            charCount[ord('a') - ord(ch)]+=1
        
        for key, ch in enumerate(t):
            charCount[ord('a') - ord(ch)]-=1
        
        for key , num in enumerate(charCount):
            if num != 0:
                return False
        return True