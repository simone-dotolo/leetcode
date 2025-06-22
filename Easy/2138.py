class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = [s[i:i+k] for i in range(0, len(s), k)  if (len(s[i:i+k]) == k)]
        if len(s) % k != 0:
            last = s[-(len(s) % k):] + fill * (k - (len(s) % k))
            res += [last]
        return res
