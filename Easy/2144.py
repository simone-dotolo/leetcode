class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        res = 0
        counter = 0
        for c in sorted(cost)[::-1]:
            counter += 1
            if counter == 3:
                counter = 0
            else:
                res += c
        return res
        
