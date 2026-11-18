class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token.isnumeric() or len(token) > 1:
                stack.append(int(token))
            else:
                r = stack.pop()
                l = stack.pop()
                if token == "/":
                    stack.append(int(l / r))
                elif token == "*":
                    stack.append(l * r)
                elif token == "+":
                    stack.append(l + r)
                else:
                    stack.append(l - r)
        return stack[0]
