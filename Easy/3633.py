class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        earliest_land = float('inf')
        for i in range(len(landStartTime)):
            earliest_land = min(earliest_land, landStartTime[i] + landDuration[i])
        
        earliest_water = float('inf')
        for i in range(len(waterStartTime)):
            earliest_water = min(earliest_water, waterStartTime[i] + waterDuration[i])
        
        res = float('inf')
        for i in range(len(landStartTime)):
            res = min(res, earliest_water + landDuration[i] + max(landStartTime[i] - earliest_water, 0))

        for i in range(len(waterStartTime)):
            res = min(res, earliest_land + waterDuration[i] + max(waterStartTime[i] - earliest_land, 0))

        return res
