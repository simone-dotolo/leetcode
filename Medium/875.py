class Solution:

    import math

    def is_valid(self, piles, h, k):

        i = 0
        while(i < len(piles)):
            if(piles[i] > 0):
                h -= math.ceil(piles[i] / k)
                i += 1

        return h >= 0

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        hours = range(1, max(piles)+1)

        start = 0
        end = len(hours) - 1
        k = 0

        while(start <= end):
     
            mid = end - (end - start)//2
            
            res = self.is_valid(piles, h, hours[mid])

            if(res):
                end = mid - 1
                k = hours[mid]
            else:
                start = mid + 1

        return k
  