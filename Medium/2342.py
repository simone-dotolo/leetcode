class Solution:

    def top_2(self, x):
        max1, max2 = -1, -1
        max1_index = -1
        for i in range(len(x)):
            if x[i] > max1:
                max1 = x[i]
                max1_index = i
        
        for i in range(len(x)):
            if x[i] > max2 and i != max1_index:
                max2 = x[i]
        
        return max1, max2

    def maximumSum(self, nums: List[int]) -> int:
        from collections import defaultdict

        count = defaultdict(list)

        for num in nums:
            sum_of_digits = sum([int(digit) for digit in str(num)])
            count[sum_of_digits].append(num)
        
        res = -1

        for key in count.keys():
            if len(count[key]) >= 2:
                a, b = self.top_2(count[key])
                res = max(res, a + b)

        return res
