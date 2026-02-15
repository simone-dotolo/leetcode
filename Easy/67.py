class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a, 2) + int(b, 2))[2:]
        a = a.zfill(len(b))
        b = b.zfill(len(a))
        res = ''
        carry = '0'
        for i in range(len(a) - 1, -1, -1):
            a_i = int(a[i], 2)
            b_i = int(b[i], 2)
            c_i = int(carry, 2)
            curr_digit = str(a_i ^ b_i ^ c_i)
            carry = str((a_i & b_i) | (b_i & c_i) | (a_i & c_i))
            res = curr_digit + res

        if carry != '0':
            res = carry + res
        
        return res
