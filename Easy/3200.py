class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
        red_first = 0
        blue_first = 0

        curr_red = red
        curr_blue = blue

        turn = 0
        while curr_red >= 0 and curr_blue >= 0:
            if turn == 0:
                curr_red -= (red_first + 1)
                if curr_red < 0:
                    red_first -= 1
                turn = 1
            else:
                curr_blue -= (red_first + 1)
                if curr_blue < 0:
                    red_first -= 1
                turn = 0
            red_first += 1
        
        curr_red = red
        curr_blue = blue

        turn = 1
        while curr_red >= 0 and curr_blue >= 0:
            if turn == 0:
                curr_red -= (blue_first + 1)
                if curr_red < 0:
                    blue_first -= 1
                turn = 1
            else:
                curr_blue -= (blue_first + 1)
                if curr_blue < 0:
                    blue_first -= 1
                turn = 0
            blue_first += 1

        return max(red_first, blue_first)