class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter

        chars = Counter(words[0])

        for word in words[1:]:
            temp_chars = Counter(word)
            remove_keys = []
            for key in chars.keys():
                if key in temp_chars.keys():
                    if chars[key] != temp_chars[key]:
                        chars[key] = min(chars[key], temp_chars[key])
                else:
                    remove_keys.append(key)
            for key in remove_keys:
                chars.pop(key)

        ans = []
        for key in chars.keys():
            for _ in range(chars[key]):
                ans.append(key)

        return ans