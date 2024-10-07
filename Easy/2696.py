class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            stack.append(char)
            if len(stack) >= 2 and (stack[-2] + stack[-1] == 'AB' or stack[-2] + stack[-1] == 'CD'):
                stack = stack[:-2]

        return len(stack) 
        
