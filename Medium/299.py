class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        dict_secret = {key:0 for key in secret}
        dict_guess = {key:0 for key in guess}
        
        for key in secret:
            dict_secret[key] += 1 
        
        for key in guess:
            dict_guess[key] += 1
        
        y = 0

        for key in set(secret):
            if key in dict_guess.keys():
                y += min(dict_guess[key],dict_secret[key])
        
        x = 0

        for i in range(len(secret)):
            if(secret[i] == guess[i]):
                x += 1

        y -= x

        return str(x)+'A'+str(y)+'B'

