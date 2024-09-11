class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        char_count = Counter(s)

        ans = 0
        odd = False
        for key in char_count.keys():
            if char_count[key] % 2 == 0:
                ans += char_count[key]
            else:
                odd = True
                ans += char_count[key] - 1

        if odd:
            ans += 1

        return ans