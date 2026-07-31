class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter

        c = Counter(word)
        res = 0
        curr = 1

        for i, char in enumerate(sorted(c, key=lambda x: c[x], reverse=True)):
            res += (i // 8 + 1) * c[char]
        
        return res
