class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        delete = []
        new_string = []
        for i, char in enumerate(s):
            new_string.append(char)
            if char == '(':
                stack.append((char,i))
            elif char == ')':
                if len(stack) != 0 and stack[-1][0] == '(':
                    stack.pop()
                else:
                    print(f'Errore carattere {i}')
                    delete.append(i)
        
        for el in delete:
            new_string[el] = 0
        for el in stack:
            new_string[el[1]] = 0
        
        print(new_string)
        return ''.join([char for char in new_string if char != 0])