class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import Counter
        
        left = 0
        right = 0
        res = 0
        count = Counter()

        while right < len(s):
            c = s[right]
            count[c] += 1

            if count[c] > 2:
                while count[c] > 2:
                    count[s[left]] -= 1
                    left += 1
            else:
                res = max(res, right - left + 1)
            
            right += 1
        
        return res
