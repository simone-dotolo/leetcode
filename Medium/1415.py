class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # A sort of arithmetic coding
        ans = ''
        num_happy_strings = 3 * 2 ** (n - 1)

        if k > num_happy_strings:
            return ans

        valid_chars = ['a', 'b', 'c']

        k -= 1

        for i in range(n):
            idx = k // (2 ** (n - i - 1))
            next_char = valid_chars[idx] 
            ans += next_char
            if next_char == 'a':
                valid_chars = ['b', 'c']
            elif next_char == 'b':
                valid_chars = ['a', 'c']
            else:
                valid_chars = ['a', 'b']
            k = k % (2 ** (n - i - 1))
        return ans
