class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def check_valid(i, dir):
            tmp_i  = i
            tmp_nums = nums[::]
            direction = dir
            while tmp_i < len(nums) and tmp_i >= 0:
                if tmp_nums[tmp_i] == 0:
                    tmp_i += direction
                else:
                    tmp_nums[tmp_i] -= 1
                    direction *= -1
                    tmp_i += direction
            
            if sum(tmp_nums) > 0:
                return False

            return True

        res = 0

        for i, num in enumerate(nums):
            if num == 0:
                res += int(check_valid(i, 1))
                res += int(check_valid(i, -1))
        return res
