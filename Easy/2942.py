class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        from collections import Counter
        indexes = []
        for i, word in enumerate(words):
            count = Counter(word)
            if count[x]:
                indexes.append(i)
        return indexes
