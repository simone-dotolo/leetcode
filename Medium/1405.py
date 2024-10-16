class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = {'a': a, 'b': b, 'c': c}

        happy = ''

        ok = True

        while ok:
            ok = False
            l = ['a', 'b', 'c']
            if len(happy) >= 2 and happy[-1] == happy[-2]:
                l.remove(happy[-1])
            argmax = None
            maxv = 0
            for el in l:
                if d[el] > maxv:
                    maxv = d[el]
                    argmax = el
            if argmax != None:
                d[argmax] -= 1
                ok = True
                happy += argmax
        
        return happy
