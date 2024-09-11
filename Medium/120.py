class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        cache = {}

        def minsum(triangle,i,j):

            if(i >= len(triangle) or j >= len(triangle[i])):
                return 0
            
            if((i,j) in cache):
                return cache[(i,j)]
            
            cache[(i,j)] = triangle[i][j] + min(minsum(triangle,i+1,j),minsum(triangle,i+1,j+1))

            return cache[(i,j)]
        
        return minsum(triangle,0,0)