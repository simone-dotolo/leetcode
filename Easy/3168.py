class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0
        curr = 0
        for event in s:
            if event == 'E':
                curr += 1
                ans = max(curr, ans)
            else:
                curr -= 1
        return ans