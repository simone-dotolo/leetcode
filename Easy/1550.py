class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cons_odds = 0
        for el in arr:
            cons_odds += (el % 2 == 1)
            cons_odds *= (el % 2 == 1)
            if cons_odds == 3:
                return True
        return False