class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while j >= 0:
            if s[j] == ' ':
                if i != 0:
                    j = -2
            else:
                i += 1
            j -= 1

        return i 