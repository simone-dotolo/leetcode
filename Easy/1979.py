class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b != 0:
                tmp = b
                b = a % b
                a = tmp
            return a

        return gcd(min(nums), max(nums))
