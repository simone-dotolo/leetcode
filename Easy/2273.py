class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        from collections import Counter

        res = [words[0]]
        ref_counter = Counter(words[0])
        
        for word in words[1:]:
            if Counter(word) != ref_counter:
                res.append(word)
                ref_counter = Counter(word)

        return res
