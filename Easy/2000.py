class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        i = 0
        ch_found = False
        new_word = []
        while i < len(word):
            if ch_found:
                new_word.append(word[i])
            else:
                new_word.insert(0,word[i])
            if word[i] == ch:
                ch_found = True
            i += 1
        
        if ch_found:
            return ''.join(new_word)
        else:
            return word