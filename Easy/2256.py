class Solution:
    def minMaxDifference(self, num: int) -> int:
        i = 0
        while i < len(str(num)) and str(num)[i] == '9':
            i += 1
        j = 0
        while j < len(str(num)) and str(num)[j] == '0':
            j += 1

        if i < len(str(num)):
            max_target_digit = str(num)[i]
            max_num = ''
            for i, digit in enumerate(str(num)):
                if digit == max_target_digit:
                    max_num += '9'
                else:
                    max_num += digit
        else:
            max_num = str(num)
            
        if j < len(str(num)):
            min_target_digit = str(num)[j]
            min_num = ''
            for i, digit in enumerate(str(num)):
                if digit == min_target_digit:
                    min_num += '0'
                else:
                    min_num += digit
        else:
            min_num = str(num)

        return int(max_num) - int(min_num)
