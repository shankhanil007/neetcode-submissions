class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # ( ) * ( ( * * 

        stack = []
        star_idx = []
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(('(', idx))
            elif ch == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                elif star_idx:
                    star_idx.remove(list(star_idx)[-1])
                else:
                    return False
            else:
                star_idx.append(idx)

        while stack:
            top_idx = stack[-1][1]
            found = False
            for idx in star_idx:
                if idx > top_idx:
                    found = True
                    stack.pop()
                    star_idx.remove(idx)
                    break
            if not found:
                return False
        if stack:
            return False
        return True


