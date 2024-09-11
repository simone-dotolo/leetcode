def tartaglia(row):

    result = list()

    row -= 1

    if row == 0:
        result.append(1)
        return result

    if row == 1:
        result.append(1)
        result.append(1)
        return result

    prev_result = tartaglia(row)

    result.append(1)

    for i in range(len(prev_result) - 1):
        result.append(prev_result[i] + prev_result[i+1])

    result.append(1)

    return result

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = list()

        for i in range(numRows):
            result.append(tartaglia(i+1))
        
        return result