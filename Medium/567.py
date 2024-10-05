class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        count = Counter(s1)

        for i in range(len(s2)):
            if s2[i] in count.keys():
                if Counter(s2[i:i+len(s1)]) == count:
                    return True
        
        return False
                    

