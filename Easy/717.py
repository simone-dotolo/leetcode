class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < (len(bits) - 1):
            if bits[i] == 1:
                i += 1
            i += 1
        
        if i == (len(bits) - 1) and bits[i] == 0:
            return True

        return False
