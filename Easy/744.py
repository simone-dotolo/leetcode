class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        right = 0
        left = len(letters) - 1

        ans = letters[0]

        while right <= left:
            mid = right + (left - right) // 2

            if ord(letters[mid]) > ord(target):
                ans = letters[mid]
                left = mid - 1
            else:
                right = mid + 1
        
        return ans
