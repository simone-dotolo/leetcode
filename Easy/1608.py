class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        for x in range(len(nums) + 1):
            count = 0
            for el in nums:
                if el >= x:
                    count += 1
            if count == x:
                return x
            print(x, count)
        
        return -1