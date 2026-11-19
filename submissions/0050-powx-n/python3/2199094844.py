class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return float(x)

        rem = 1
        if n%2 == 1:
            rem = x
        
        ans = self.myPow(x, (abs(n)//2))
        ans = ans * ans * rem
        if n < 0:
            return 1.0 / float(ans)
        else:
            return ans
        

        
