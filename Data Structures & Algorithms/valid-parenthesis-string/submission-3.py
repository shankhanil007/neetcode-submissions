class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        star = []
        for idx,ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
            elif ch == '*':
                star.append(idx)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False

        if stack:
            if len(stack) > len(star):
                return False
            for i in range(len(stack)-1, -1, -1):
                if stack[i] > star[-1]:
                    return False
                star.pop()
        return True
        