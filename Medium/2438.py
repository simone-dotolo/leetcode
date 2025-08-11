class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        from math import floor, log
        powers = []
        nbits = floor(log(n, 2)) + 1
        for i, bindigit in enumerate(bin(n)[2:]):
            if int(bindigit):
                powers.append(2 ** (nbits - 1 - i))
        
        powers = powers[::-1]

        cum_powers = [powers[0]]
        for i in range(1, len(powers)):
            cum_powers.append(cum_powers[-1] * powers[i])
        
        res = []
        for left, right in queries:
            if left != 0:
                value = int((cum_powers[right] // cum_powers[left - 1]) % (1e9 + 7))
                res.append(value)
            else:
                value = int(cum_powers[right] % (1e9 + 7))
                res.append(value)
        
        return res
