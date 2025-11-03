class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = neededTime[0]
        curr = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                curr = max(curr, neededTime[i])
            else:
                res -= curr
                curr = neededTime[i]
            res += neededTime[i]
        res -= curr

        return res
