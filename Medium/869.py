class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter
        powers = [Counter(str(2 **  i)) for i in range(31)]
        return Counter(str(n)) in powers
        
