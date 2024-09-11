class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        for char in s:
            if char == '(':
                stack.append(char)
                if len(stack) > max_depth:
                    max_depth = len(stack)
            elif char == ')':
                if len(stack) == 0:
                    return None
                else:
                    stack.pop()
        return max_depth