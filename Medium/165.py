class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vs1 = [int(el) for el in version1.split('.')]
        vs2 = [int(el) for el in version2.split('.')]

        num_revisions = max(len(vs1), len(vs2))

        vs1 += ([0] * (num_revisions - len(vs1)))
        vs2 += ([0] * (num_revisions - len(vs2)))

        for v1, v2 in zip(vs1, vs2):
            if v1 < v2: return -1
            elif v1 > v2: return 1
        
        return 0
