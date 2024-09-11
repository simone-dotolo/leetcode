class Solution:
    def getLucky(self, s: str, k: int) -> int:
        offset = 96
        transformed_s = ''

        for ch in s:
            transformed_s += str(ord(ch) - offset)

        for _ in range(k):
            transformed_s = sum([int(el) for el in str(transformed_s)])
        
        return transformed_s