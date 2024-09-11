class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum([int(x) for x in str(bin(x ^ y))[2:]])