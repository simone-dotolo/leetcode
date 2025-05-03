class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        min_swaps = len(tops) + 1

        # make tops[0] in top row
        curr_swaps = 0 
        target = tops[0]
        is_possible = True
        i = 1
        while is_possible and i < len(tops):
            if tops[i] == target:
                i += 1
                continue
            elif bottoms[i] == target:
                curr_swaps += 1
            else:
                is_possible = False
                curr_swaps = len(tops) + 1
            i += 1
        min_swaps = min(min_swaps, curr_swaps)

        # make tops[0] in bottom row
        curr_swaps = 1 
        target = tops[0]
        is_possible = True
        i = 1
        while is_possible and i < len(bottoms):
            if bottoms[i] == target:
                i += 1
                continue
            elif tops[i] == target:
                curr_swaps += 1
            else:
                is_possible = False
                curr_swaps = len(bottoms) + 1
            i += 1
        min_swaps = min(min_swaps, curr_swaps)

        # make bottoms[0] in bottom row
        curr_swaps = 0
        target = bottoms[0]
        is_possible = True
        i = 1
        while is_possible and i < len(bottoms):
            if bottoms[i] == target:
                i += 1
                continue
            elif tops[i] == target:
                curr_swaps += 1
            else:
                is_possible = False
                curr_swaps = len(bottoms) + 1
            i += 1
        min_swaps = min(min_swaps, curr_swaps)

        # make bottoms[0] in top row
        curr_swaps = 1 
        target = bottoms[0]
        is_possible = True
        i = 1
        while is_possible and i < len(tops):
            if tops[i] == target:
                i += 1
                continue
            elif bottoms[i] == target:
                curr_swaps += 1
            else:
                is_possible = False
                curr_swaps = len(tops) + 1
            i += 1
        min_swaps = min(min_swaps, curr_swaps)

        return min_swaps if min_swaps != (len(tops) + 1) else -1
