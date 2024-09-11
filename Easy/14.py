class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def shortest_prefix(shortest_string, min_length, strings):

            res = ''

            for i in range(min_length):
                nomatch = False
                for string in strings:
                    if(string[i] != shortest_string[i]):
                        nomatch = True
                if(nomatch is False):
                    res += shortest_string[i]
                else:
                    break
            
            return res

        from math import inf

        min_length = inf
        min_index = 0
        for i in range(len(strs)):
            if(len(strs[i]) < min_length):
                min_length = len(strs[i])
                min_index = i

        shortest_string = strs[min_index]

        return shortest_prefix(shortest_string, min_length, strs)