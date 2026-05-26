class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        from collections import Counter
        res = 0
        c1, c2 = Counter(word), Counter(word.lower())
        for k1 in c1.keys():
            if c2[k1] and c1[k1] != c2[k1]:
                res += 1
        return res
