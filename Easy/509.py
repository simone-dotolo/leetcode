class Solution:
    memo = {}
    def fib(self, n: int) -> int:
        f = 0
        if n in self.memo.keys():
            return self.memo[n]
        elif n == 0:
            f = 0
        elif n == 1:
            f = 1
        else:
            f = self.fib(n-1) + self.fib(n-2)
        self.memo[n] = f
        return f