class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        cache = {}

        def wordbreak(string,dic,i):

            if(i == len(string)):
                return True
            
            if(i in cache):
                return cache[i]

            for words in dic:
                if(string[i:i+len(words)] == words):
                    cache[i] = True
                    if(wordbreak(string,dic,i+len(words))):
                        return True
                    else:
                        cache[i] = False

            return False
        
        return wordbreak(s,wordDict,0)