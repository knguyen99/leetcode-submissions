class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                word = s[i:i+2]
                if word == "CD":
                    total += 400
                    i += 2
                elif word == "CM":
                    total += 900
                    i += 2
                elif word == "XL":
                    total += 40
                    i += 2
                elif word == "XC":
                    total += 90
                    i += 2
                elif word == "IV":
                    total += 4
                    i += 2
                elif word == "IX":
                    total += 9
                    i += 2
                else:
                    total += d[s[i]]
                    i += 1
            else:
                total += d[s[i]]
                i += 1
        return total