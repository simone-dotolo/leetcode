class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        lows = []
        highs = []

        for num in nums:
            # Update lows
            if len(lows) < 2:
                lows.append(num)
            elif num < lows[1]:
                lows[1] = num
            
            lows.sort()
            
            # Update highs
            if len(highs) < 3:
                highs.append(num)
            elif num > highs[0]:
                highs[0] = num

            highs.sort()
        
        return max(highs[2] * lows[0] * lows[1], highs[2] * highs[0] * highs[1])
