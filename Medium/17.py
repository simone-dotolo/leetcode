class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        
        nums = [int(x) for x in digits]
        
        if(len(nums) == 0):
            return []
        
        if(len(nums) == 1):
            if(nums[0] == 2):
                return ['a','b','c']
            elif(nums[0] == 3):
                return ['d', 'e', 'f']
            elif(nums[0] == 4):
                return ['g', 'h', 'i']
            elif(nums[0] == 5):
                return ['j', 'k', 'l']
            elif(nums[0] == 6):
                return ['m', 'n', 'o']
            elif(nums[0] == 7):
                return ['p', 'q', 'r', 's']
            elif(nums[0] == 8):
                return ['t', 'u', 'v']
            elif(nums[0] == 9):
                return ['w', 'x', 'y', 'z']
            
        n = nums.pop(0)
        
        new_digits = ''
        
        for num in nums:
            new_digits += str(num)
        
        subsets = self.letterCombinations(new_digits)
        
        if(n == 2):
            for subset in subsets:
                res.append('a'+subset)
                res.append('b'+subset)
                res.append('c'+subset)
        elif(n == 3):
            for subset in subsets:
                res.append('d'+subset)
                res.append('e'+subset)
                res.append('f'+subset)
        elif(n == 4):
            for subset in subsets:
                res.append('g'+subset)
                res.append('h'+subset)
                res.append('i'+subset)
        elif(n == 5):
            for subset in subsets:
                res.append('j'+subset)
                res.append('k'+subset)
                res.append('l'+subset)
        elif(n == 6):
            for subset in subsets:
                res.append('m'+subset)
                res.append('n'+subset)
                res.append('o'+subset)
        elif(n == 7):
            for subset in subsets:
                res.append('p'+subset)
                res.append('q'+subset)
                res.append('r'+subset)
                res.append('s'+subset)
        elif(n == 8):
            for subset in subsets:
                res.append('t'+subset)
                res.append('u'+subset)
                res.append('v'+subset)
        elif(n == 9):
            for subset in subsets:
                res.append('w'+subset)
                res.append('x'+subset)
                res.append('y'+subset)
                res.append('z'+subset)
        
        return res