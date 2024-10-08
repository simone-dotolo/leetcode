class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance = 0

        for char in s:
            if char == ']':
                imbalance += ((-1)**(imbalance > 0))
            else:
                imbalance += 1
        
        return (imbalance + 1) // 2
        
