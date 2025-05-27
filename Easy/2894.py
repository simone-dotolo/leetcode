class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1, n + 1):
            num1 += (i % m != 0) * i
            num2 += (i % m == 0) * i
        return num1 - num2
        
