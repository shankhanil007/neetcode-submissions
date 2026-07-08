class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(token)
            else:
                num2 = int(stack[-1])
                stack.pop()
                num1 = int(stack[-1])
                stack.pop()

                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2)) ## IMP
        return int(stack[-1]) ## IMP when there is only 1 token ["18"]
                    