class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for j, word in enumerate(sentence.split()):
            if len(word) >= len(searchWord):
                i = 0
                match = (word[i] == searchWord[i])
                while match:
                    match = (word[i] == searchWord[i])
                    i += 1
                    if match and i == len(searchWord):
                        print(word)
                        return j + 1
        return -1
