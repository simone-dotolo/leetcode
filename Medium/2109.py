class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        curr_space = 0

        for i, char in enumerate(s):
            if curr_space < len(spaces) and i == (spaces[curr_space]):
                res += ' '
                curr_space += 1
            res += char

        return res 
        
