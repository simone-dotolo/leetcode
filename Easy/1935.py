class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        res = len(words)
        for word in words:
            i = 0
            while i < len(word):
                if word[i] in brokenLetters:
                    res -= 1
                    i = len(word)
                i += 1
        return res
        
