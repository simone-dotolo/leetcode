class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: 50 * x[1] - x[0], reverse=True)
        res = 0
        for i in range(len(points)):
            max_x = 51
            for j in range(i + 1, len(points)):
                if (points[i][0] <= points[j][0] and points[j][0] < max_x):
                    res += 1
                    max_x = points[j][0]
        return res
