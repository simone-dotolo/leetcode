class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            word = set(word)
            all_chars_allowed = True
            for char in word:
                if char not in allowed:
                    all_chars_allowed = False
                    break
            res += all_chars_allowed
        return res
