class Solution:
    def binaryGap(self, n: int) -> int:
        max_dist = 0 
        prev_one = 0

        for i, digit in enumerate(bin(n)[2:]):
            if digit == '1':
                max_dist = max(max_dist, i - prev_one)
                prev_one = i

        return max_dist
