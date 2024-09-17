from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counts = Counter([s for s in s1.split()] + [s for s in s2.split()])
        return [el for el in counts if counts[el] == 1]
