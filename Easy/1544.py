class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) != 0:
                if stack[-1] != char and stack[-1].lower() == char.lower():
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        return ''.join(stack)