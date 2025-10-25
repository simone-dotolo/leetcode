class Solution:
    def totalMoney(self, n: int) -> int:
        week = 28
        n_weeks = n // 7
        last_days = n % 7
        return week * n_weeks + 7 * n_weeks * (n_weeks - 1) // 2 + sum([i + n_weeks + 1 for i in range(last_days)])
