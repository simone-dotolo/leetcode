class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for char in s:
            if char.isdigit() and len(res) > 0:
                res.pop()
            else:
                res.append(char)
        return ''.join(res)
