class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        i = 0
        while i < k:
            inc = happiness[i] - i
            ans += max(0, inc)
            i += 1
        return ans