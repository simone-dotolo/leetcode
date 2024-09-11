class Solution:
    def maximum69Number (self, num: int) -> int:

        for i in range(len(str(num))):
            if(str(num)[i] == '6'):
                num += 3 * 10 ** (len(str(num)) - 1 - i)
                return num
        
        return num