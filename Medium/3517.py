class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter

        res = ''
        odd_char = None
        idx = -1
        curr = 0

        c = Counter(s)

        for k in sorted(c.keys()):
            if c[k] % 2 != 0:
                odd_char = k
                idx = curr
            else:
                res += k * (c[k] // 2)
                curr += c[k] // 2
                
        if odd_char is not None:
            res = res[:idx] \
            + odd_char * ((c[odd_char] - 1) // 2) \
            + res[idx:] \
            + odd_char \
            + res[idx:][::-1] \
            + odd_char * ((c[odd_char] - 1) // 2) \
            + res[:idx][::-1]
        else:
            res += res[::-1]

        return res
