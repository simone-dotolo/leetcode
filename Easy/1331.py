class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        def find_el(arr, el):
            low = 0
            high = len(arr) - 1
            idx = -1

            while low <= high:
                mid = low + (high - low) // 2

                if arr[mid] == el:
                    idx = mid
                    high = mid - 1
                elif arr[mid] < el:
                    low = mid + 1
                else:
                    high = mid - 1

            return idx

        sorted_arr = sorted(set(arr))

        res = []

        for el in arr:
            idx = find_el(sorted_arr, el)
            res.append(idx + 1)
        
        return res
