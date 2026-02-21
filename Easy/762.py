class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum([num.bit_count() in [2, 3, 5, 7, 11, 13, 17, 19] for num in range(left, right + 1)])
