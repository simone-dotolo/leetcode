class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        for key, value in c.items():
            if value % 2 != 0:
                return False
        return True
        
