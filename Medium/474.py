class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = dict()
        zeros = []
        for str_ in strs:
            count = 0
            for el in str_:
                count += (el == '0')
            zeros.append(count)

        def dp(i, m, n):
            if i >= len(strs) or m < 0 or n < 0:
                return 0
            
            if res := cache.get((i, m, n)):
                return res

            n_zeros = zeros[i]
            n_ones = len(strs[i]) - n_zeros

            if m - n_zeros >= 0 and n - n_ones >= 0:
                cache[(i, m, n)] = max(1 + dp(i + 1, m - n_zeros, n - n_ones), dp(i + 1, m, n))
            else:
                cache[(i, m, n)] = dp(i + 1, m, n)

            return cache[(i, m, n)]
        
        return dp(0, m, n)
