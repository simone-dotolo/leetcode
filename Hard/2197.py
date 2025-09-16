class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)
        
        def is_non_coprime(x, y):
            return gcd(x, y) > 1
        
        stack = []

        for num in nums:
            if len(stack) == 0 or not is_non_coprime(stack[-1], num):
                stack.append(num)
            else:
                while len(stack) != 0 and is_non_coprime(stack[-1], num):
                    num = int(num * stack[-1] / gcd(stack[-1], num))
                    stack.pop()
                stack.append(num)
        return stack
