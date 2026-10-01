class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in [')', ']', '}']:
                if stack and abs(ord(stack[-1]) - ord(c)) <= 2:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
