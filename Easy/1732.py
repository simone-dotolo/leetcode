class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        curr = 0
        for el in gain:
            curr += el
            res = max(res, curr)
        return res
