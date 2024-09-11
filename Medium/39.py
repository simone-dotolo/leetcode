class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def is_valid(nums, target):
            return sum(nums) < target
        
        def is_solution(nums, target):
            return sum(nums) == target
        
        res = []
        partial_sum = []
        
        def solve(nums, target, res, partial_sum,index):
            
            for i in range(index,len(nums)):
                partial_sum.append(nums[i])
                if(is_valid(partial_sum,target)):
                    solve(nums, target, res, partial_sum,i)
                elif(is_solution(partial_sum,target)):
                    res.append(partial_sum.copy())
                partial_sum.pop()
            
        solve(candidates, target, res, partial_sum,0)      
        
        return res