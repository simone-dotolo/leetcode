class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        stack = []
        res = ''

        knowledge = {k: v for (k, v) in knowledge}

        for c in s:
            if stack or c == '(':
                stack.append(c)

                if stack[-1] == ')':
                    key = stack[1:-1]
                    stack = []
                    res += knowledge.get(''.join(key), '?')
            else:
                res += c
        
        return res
