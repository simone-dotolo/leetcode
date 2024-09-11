class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return sum([1 for el in bin(start ^ goal) if el == '1'])
