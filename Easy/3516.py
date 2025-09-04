class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return min([(abs(x - z), 1), 
                    (abs(y - z), 2), 
                    (-1 * (abs(x - z) == abs(y - z)) + 101 * (abs(x - z) != abs(y - z)), 0)], key=lambda x: x[0])[1]

        
