class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        res = 0
        i = 0
        while(i < len(strs[0])):
            j = 0
            last_char = ' '
            while(j < len(strs)):
                if(strs[j][i] < last_char):
                    res += 1
                    j = len(strs)
                else:
                    last_char = strs[j][i]
                    j += 1
            i += 1

        return res