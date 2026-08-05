class Solution:
    def isValid(self, s: str) -> bool:
        charMap  = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []
        for ch in s:
            if ch in charMap:
                if stack and stack[-1] == charMap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False
