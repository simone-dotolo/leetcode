class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = [int(num, 2) for num in nums]
        for i in range(2 ** len(nums)):
            if i not in nums:
                return bin(i)[2:].zfill(len(nums))
