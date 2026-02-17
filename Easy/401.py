class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        def bits_to_h_m(bits: str) -> tuple[int, int]:
            h, m = 0, 0

            for i in range(4):
                h += int(bits[i]) * (2 ** (3 - i))

            for i in range(6):
                m += int(bits[-i-1]) * (2 ** i)

            return h, m

        def time_comb(turned_on: int) -> list[str]:
            res = []

            for i in range(1024):
                bits = bin(i)[2:].zfill(10)
                if bits.count('1') == turned_on:
                    h, m = bits_to_h_m(bits)
                    if h < 12 and m < 60:
                        res.append(f'{h}:{str(m).zfill(2)}')
            
            return res
        
        return time_comb(turnedOn)
