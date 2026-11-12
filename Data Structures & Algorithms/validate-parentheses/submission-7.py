class Solution:
    def isValid(self, s: str) -> bool:
        
        hmap = {'}': '{', ']': '[', ')': '(',}
        stack = []
        for ch in s:
            if ch in ['{', '(', '[']:
                stack.append(ch)
            else:
                if not stack or stack[-1] != hmap[ch]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True

