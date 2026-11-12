class Solution:
    def isValid(self, s: str) -> bool:
        
        hmap = {'}': '{', ']': '[', ')': '(',}
        stack = []
        for ch in s:
            if ch in ['{', '(', '[']:
                stack.append(ch)
            else:
                if len(stack)==0 or (stack and stack[-1] != hmap[ch]):
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True

