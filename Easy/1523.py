class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1) // 2 + int(low & high & 1)
