class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # O(m*log(m) + n*log(m))
        def smallest_potion(potions, target):
            start = 0
            end = len(potions) - 1
            res = len(potions)
            while start <= end:
                mid = start + (end - start) // 2
                if potions[mid] >= target:
                    res = mid
                    end = mid - 1
                else:
                    start = mid + 1
            return res
        
        from math import ceil
        potions.sort()
        pairs = []
        for spell in spells:
            target = ceil(success / spell)
            # Find the smallest potion with value >= target and its index
            index = smallest_potion(potions, target)
            n_potions = len(potions) - index
            pairs.append(n_potions)
        return pairs
