class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mins = []
        maxs = []
        for num in nums:
            if len(mins) < 2:
                mins.append(num)
            elif num < mins[1]:
                mins[1] = num
            mins.sort()

            if len(maxs) < 2:
                maxs.append(num)
            elif num > maxs[0]:
                maxs[0] = num
            maxs.sort()

        return max(mins[0] * mins[1] - mins[0] - mins[1] + 1, maxs[0] * maxs[1] - maxs[0] - maxs[1] + 1)
        
