class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        prefix_xor = []
        last = 0

        for i in range(len(arr)):
            last ^= arr[i]
            prefix_xor.append(last)
        
        res = []

        for query in queries:
            left = query[0]
            right = query[1]

            if left == 0:
                res.append(prefix_xor[right])
            else:
                res.append(prefix_xor[right] ^ prefix_xor[left - 1])
            
        return res
        
