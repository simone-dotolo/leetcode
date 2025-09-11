class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        counter = {vowel: 0 for vowel in vowels}

        for char in s:
            if char in vowels:
                counter[char] += 1
        
        stack = []
        for vowel in vowels[::-1]:
            stack.extend([vowel] * counter[vowel])
    
        s = [char for char in s]

        if stack:
            for i, char in enumerate(s):
                if char in vowels:
                    s[i] = stack.pop()

        return ''.join(s)
