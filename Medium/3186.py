class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cache = {}
        power.sort()

        def dp(i):
            if i >= len(power):
                return 0
            
            if res := cache.get(i):
                return res
            
            j = i + 1
            count = 1
            while j < len(power) and power[j] <= power[i] + 2:
                if power[j] == power[i]:
                    count += 1
                j += 1

            cache[i] = max(power[i] * count + dp(j), dp(i + count))

            return cache[i]
        
        return dp(0)
