class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        def make_move(nums,position,path):
            path.append(nums[position])

        def unmake_move(path):
            path.pop()

        def is_valid(choice):
            return choice == 1

        def is_solution(path,res):
            return path not in res

        def solve(nums,position,choice,path,res):
            
            if(is_valid(choice) is False):
                return

            make_move(nums,position,path)

            if(is_solution(path,res)):
                res.append(path.copy())
            
            for i in range(position+1,len(nums)):
                solve(nums,i,0,path,res)
                solve(nums,i,1,path,res)

            unmake_move(path)

            return

        path = []
        res = []

        for i in range(len(nums)):
            solve(nums,i,0,path,res)
            solve(nums,i,1,path,res)

        res.append([])

        return res