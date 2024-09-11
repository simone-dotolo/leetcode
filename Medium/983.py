class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        cache = {}

        def mincost(days,cost,i):

            if(i >= len(days)):
                return 0

            if(i in cache):
                return cache[i]
            
            j = i+1
            while(j < len(days) and days[j] < days[i] + 7):
                j += 1
            
            k = i+1
            while(k < len(days) and days[k] < days[i] + 30):
                k += 1
            
            cache[i] = min(cost[0] + mincost(days,cost,i+1), cost[1] + mincost(days,cost,j), cost[2] + mincost(days,cost,k))

            return cache[i]

        return mincost(days,costs,0)