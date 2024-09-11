class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        def is_root(root, word):
            if len(root) > len(word):
                return False
            
            for i in range(len(root)):
                if root[i] != word[i]:
                    return False
            
            return True

        dictionary.sort(key=lambda x: len(x))
        
        res = []

        words = sentence.split(' ')

        for word in words:
            root_found = False
            for root in dictionary:
                if root_found == False and is_root(root, word):
                    res.append(root)
                    root_found = True
            if root_found == False:
                res.append(word)

        print(res)

        return ' '.join(res)