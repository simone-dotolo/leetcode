class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(set(s)) != len(set(t)):
            return False

        corr = {}
        for i in range(len(s)):
            if s[i] not in corr.keys():
                corr[s[i]] = t[i]
        
        new_s = ''.join([corr[char] for char in s])

        print(new_s)

        return new_s == t