class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        MOD = 10 ** 9 + 7

        values = [x for x in range(1,k+1)]

        cache = {}

        def dp(j,i):

            if(j == n and i == target):
                return 1

            if(j > n or i > target):
                return 0
            
            if((j,i) in cache):
                return cache[(j,i)]
            
            cache[(j,i)] = sum([dp(j+1,i+values[z]) for z in range(len(values))])

            return cache[(j,i)]

        return int(dp(0,0) % MOD)
        