class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict

        res = float('inf')
        d = defaultdict(list)

        for i, num in enumerate(nums):
            d[num].append(i)
        
        for k, v in d.items():
            for i in range(len(v) - 2):
                tmp = v[i:i+3]
                res = min(res, 2 * (tmp[2] - tmp[0]))

        return res if res != float('inf') else -1
