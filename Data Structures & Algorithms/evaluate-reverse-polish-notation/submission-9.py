import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operation = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for i in tokens:
            if i not in operation:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(operation[i](a, b))

        return stack[0]
                
            