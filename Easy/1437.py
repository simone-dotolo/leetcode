class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        curr_k = k
        for num in nums:
            if num and curr_k < k:
                return False
            curr_k = curr_k * (1 - int(num == 1)) + int(num == 0)
        return True
