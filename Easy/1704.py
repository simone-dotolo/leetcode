class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        def count_vowels(s):
            count = 0
            for char in s:
                if(char in vowels):
                    count += 1
            return count

        return count_vowels(s[:len(s)//2]) == count_vowels(s[len(s)//2:])