def search_last_el(array, element):

    last_index = -1

    low = 0
    high = len(array) - 1

    while(low <= high):

        mid = int((high - low) / 2 + low)

        if(array[mid] > element):
            high = mid - 1
        elif(array[mid] == element):
            last_index = mid
            high = mid - 1
        else:
            low = mid + 1

    return last_index

class Solution:

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_array = sorted(nums)
        res = list()

        for i in range(len(nums)):

            n = search_last_el(sorted_array, nums[i])

            res.append(n)

        return res