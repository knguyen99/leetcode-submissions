class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        #mark a as the longer string
        if len(b) > len(a):
            a, b = b, a
            
        a = a[::-1]
        b = b[::-1]
        
        pa = 0
        pb = 0
        
        carry = 0
        ret = ""
        while pb < len(b):
            ai = 1 if a[pa] == "1" else 0
            bi = 1 if b[pb] == "1" else 0
            curr = ai + bi + carry
            ret += "1" if curr%2 == 1 else "0"
            carry = 1 if curr > 1 else 0
            pa += 1
            pb += 1
            
        while pa < len(a):
            ai = 1 if a[pa] == "1" else 0
            curr = ai + carry
            ret += "1" if curr%2 == 1 else "0"
            carry = 1 if curr > 1 else 0
            pa += 1
            
        if carry == 1:
            ret += "1"
        return ret[::-1]