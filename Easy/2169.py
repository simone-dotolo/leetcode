class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0
        while num1 * num2:
            num1, num2 = max(num1, num2), min(num1, num2)
            res += (num1 // num2)
            num1 -= (num1 // num2 * num2)
        return res
