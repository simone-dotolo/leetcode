class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        res = 1
        max_r = intervals[0][1]

        for l, r in intervals[1:]:
            if r > max_r:
                res += 1
                max_r = r
        
        return res
