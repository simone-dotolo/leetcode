class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = [0 for _ in range(100_001)]
        for cost in costs:
            counts[cost] += 1
        
        res = 0
        for i, count in enumerate(counts[1:], 1):
            if count and i * count < coins:
                res += count
                coins -= (i * count)
            elif count:
                res += (coins // i)
                break
        return res
