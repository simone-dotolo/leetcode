class Solution:
    def judgeCircle(self, moves: str) -> bool:
        s = 0
        for move in moves:
            if move == 'L':
                s -= 1
            elif move == 'R':
                s += 1
            elif move == 'D':
                s -= 1e6
            elif move == 'U':
                s += 1e6
        return s == 0
