class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # ( ) * ( ( * * 

        stack = []
        star = []
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
            elif ch == ')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(idx)

        while stack and star:        ##### IIMMMPPP while loop
            if stack[-1] > star[-1]:
                return False
            stack.pop()
            star.pop()

        if stack:
            return False
        return True


