class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        min_diff = float('inf')

        arr.sort()

        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) < min_diff:
                min_diff = abs(arr[i] - arr[i - 1])
                res = [[arr[i - 1], arr[i]]]
            elif abs(arr[i] - arr[i - 1]) == min_diff:
                res.append([arr[i - 1], arr[i]])
        
        return res
