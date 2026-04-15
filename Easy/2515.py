class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res = float('inf')
        n = len(words)
        for i, word in enumerate(words):
            if word == target:
                res = min(res, abs(i - startIndex), n - abs(i - startIndex))
        return res if res != float('inf') else -1
