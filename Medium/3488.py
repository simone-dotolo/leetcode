class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    return mid
            
            return -1

        from collections import defaultdict

        d = defaultdict(list)

        for i, num in enumerate(nums):
            d[num].append(i)

        res = []
        n = len(nums)
        for query in queries:
            target = nums[query]
            distance = float('inf')
            index = binary_search(d[target], query)
            distance = min(distance,
                           abs(d[target][(index+1)%len(d[target])] - query),
                           n - abs(d[target][(index+1)%len(d[target])] - query),
                           abs(d[target][(index-1)%len(d[target])] - query),
                           n - abs(d[target][(index-1)%len(d[target])] - query))
            res.append(distance if distance != 0 else -1)
        return res
