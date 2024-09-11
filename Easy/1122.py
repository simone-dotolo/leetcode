class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        curr_pos = 0
        count = 0
        for num in arr2:
            for i in range(len(arr1)):
                if arr1[i] == num:
                    arr1[i], arr1[curr_pos] = arr1[curr_pos], arr1[i]
                    count += 1
                    curr_pos += 1
        
        start = count
        end = len(arr1)

        for _ in range(end - start):
            for i in range(start, end - 1):
                if arr1[i] > arr1[i+1]:
                    arr1[i], arr1[i+1] = arr1[i+1], arr1[i]

        return arr1
        