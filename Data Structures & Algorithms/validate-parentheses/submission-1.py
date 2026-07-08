class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {']':'[', '}':'{', ')': '('}
        for ch in s:
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)
            else:
                if len(stack) == 0 or stack[-1] != hmap[ch]:
                    return False
                stack.pop()
        return len(stack) == 0
        