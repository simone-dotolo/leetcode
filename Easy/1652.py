class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        if k == 0:
            return [0] * len(code)
        if k > 0:
            code.reverse()

        start = len(code) - abs(k)
        cumsum = sum(code[start:])
        for i in range(len(code)):
            res.append(cumsum)
            cumsum = cumsum - code[start] + code[i]
            start += 1
            if start >= len(code):
                start = start % len(code)
        
        if k > 0:
            res.reverse()

        return res
