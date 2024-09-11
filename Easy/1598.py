class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if len(stack) > 0 and log == '../':
                stack.pop()
            elif log != './' and log != '../':
                stack.append(log)
        
        return len(stack)
        