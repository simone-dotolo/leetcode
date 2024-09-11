class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        d = {}

        for i in range(len(arr)):
            if(arr[i] not in d):
                d[arr[i]] = 1
            else:
                d[arr[i]] += 1
        
        occ = [d[key] for key in d.keys()]

        return len(occ) == len(set(occ))