class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0 for _ in range(10001)]
        for num in nums:
            if count[num]:
                return num
            else:
                count[num] += 1
        return -1
