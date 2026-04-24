class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        res = 0
        count = 0
        for move in moves:
            if move == 'L':
                res -= 1
            elif move == 'R':
                res += 1
            else:
                count += 1
        
        return abs(res) + count
