class Solution:
    def compressedString(self, word: str) -> str:

        res = []

        count = 0
        last = ''
        
        for i in range(0, len(word)):
            if word[i] == last:
                count += 1
            else:
                res.append([last, count])
                last = word[i]
                count = 1
            if i == len(word) - 1:
                res.append([last, count])

        output = ''
        for i in range(1, len(res)):
            char, count = res[i]
            while count > 9:
                count -= 9
                output += f'9{char}'
            output += f'{count}{char}'

        return output
            
