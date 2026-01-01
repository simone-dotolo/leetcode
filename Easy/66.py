class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(el) for el in str(int(''.join(str(el) for el in digits)) + 1)]
