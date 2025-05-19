class Solution:
    def triangleType(self, nums: List[int]) -> str:
        def admissable(nums):
            if (nums[0] + nums[1] <= nums[2]) or (nums[0] + nums[2] <= nums[1]) or (nums[1] + nums[2] <= nums[0]):
                return False
            else:
                return True
        
        sides = set()
        for num in nums:
            sides.add(num)
        
        types = ['equilateral', 'isosceles', 'scalene']

        if admissable(nums):
            return types[len(sides) - 1]
        else:
            return 'none'

        
