class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        n = len(directions)

        curr_right = 0
        curr_left = 0
t
        for i in range(n):
            # Going from left to right, if we hit S or L, increase by the number of cars going to the right
            # else increase the number of cars going to the right
            # the same applies for cars going from right to left
            res += (directions[i] != 'R') * curr_right + (directions[n - 1 - i] != 'L') * curr_left
            curr_right = (directions[i] == 'R') * (curr_right + 1)
            curr_left = (directions[n - 1 - i] == 'L') * (curr_left + 1) 
        
        # Time: O(n)
        # Space: O(1)
        return res
