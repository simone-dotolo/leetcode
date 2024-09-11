class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(2**n):
            mask = [int(el) for el in bin(i).split('b')[1]]
            if len(mask) < n:
                mask = [0]*(n-len(mask)) + mask
            tmp = 0
            for j in range(len(mask)):
                if mask[j]:
                    tmp = tmp ^ nums[j]
            ans += tmp
        
        return ans