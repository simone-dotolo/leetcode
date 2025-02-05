class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_count = 0
        first_diff = -1
        second_diff = -1

        for i in range(len(s2)):
            if s2[i] != s1[i]:
                diff_count += 1
                if first_diff != -1:
                    second_diff = i
                else:
                    first_diff = i
        
        return (diff_count == 2 and s1[first_diff] == s2[second_diff] and s1[second_diff] == s2[first_diff]) or (diff_count == 0)
