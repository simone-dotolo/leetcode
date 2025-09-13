class Solution:
    def maxFreqSum(self, s: str) -> int:
        freqs = [0 for _ in range(26)]
        
        for char in s:
            freqs[ord(char) - 97] += 1
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_vowel_freq = 0
        for vowel in vowels:
            max_vowel_freq = max(max_vowel_freq, freqs[ord(vowel) - 97])
            freqs[ord(vowel) - 97] = 0
        
        return max_vowel_freq + max(freqs)
