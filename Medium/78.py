class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        for mask in range(2**n):
            mask = bin(mask).split('b')[1]

            if len(mask) < n:
                mask = '0'*(n - len(mask)) + mask

            new_subset = []

            for i in range(len(mask)):
                if mask[i] == '1':
                    new_subset.append(nums[i])
            
            ans.append(new_subset)

        return ans