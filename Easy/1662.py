class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        w1 = ""
        w2 = ""
        
        for el in word1:
            w1 += el
        for el in word2:
            w2 += el
            
        return w1 == w2