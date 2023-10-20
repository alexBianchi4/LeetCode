# Time Complexity : O(n)
# Space Complexity: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                y,x = stack.pop(),stack.pop()
                stack.append(x - y)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                y,x = stack.pop(),stack.pop()
                stack.append(int(x / y))
            else:
                stack.append(int(token))
        return stack.pop()