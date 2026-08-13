class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+','-','*','/'}
        stack = []
        for t in tokens:
            if t in operations:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if t == '+': stack.append(num1 + num2)
                elif t == '-': stack.append(num1 - num2)
                elif t == '*': stack.append(num1 * num2)
                else: stack.append(int(num1 / num2))
            else:
                stack.append(t)
        return int(stack[-1])