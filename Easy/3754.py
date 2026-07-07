class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0 
            
        cumsum = 0
        new_n = []
        while n:
            digit = n % 10
            if digit:
                new_n.append(digit)
            cumsum += digit
            n //= 10
        return int(''.join(str(el) for el in new_n[::-1])) * cumsum
