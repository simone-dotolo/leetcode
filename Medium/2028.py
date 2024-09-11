class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_of_n = mean * (len(rolls) + n) - sum(rolls)
        
        res = []

        if sum_of_n // n > 6 or sum_of_n <= 0:
            return []
        
        for _ in range(n):
            res.append(sum_of_n // n)
        
        residual = sum_of_n % n

        print(res, residual)

        for i in range(len(res)):
            if res[i] < 6 and residual > 0:
                sub = min((6 - res[i]), residual)
                res[i] += sub
                residual -= sub
                
        if not residual and (0 not in res):
            return res
        
        return []