class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars_info = [None for _ in range(26)]

        ord_a = ord('a')
        for char in word:
            ord_char = ord(char)
            if ord_char < 91:
                if not chars_info[ord_char % 65]:
                    chars_info[ord_char % 65] = 'u'
                elif chars_info[ord_char % 65] == 'l':
                    chars_info[ord_char % 65] += 'u'
            else:
                if not chars_info[ord_char % 97]:
                    chars_info[ord_char % 97] = 'l'
                elif chars_info[ord_char % 97] == 'lu':
                    chars_info[ord_char % 97] = 'x'

        res = 0
        for el in chars_info:
            res += int(el == 'lu')
        
        return res
