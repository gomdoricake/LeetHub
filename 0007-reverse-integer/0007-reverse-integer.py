class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: 
            s = str(-1 * x)
            sign = "-"
        else: 
            s = str(x)
            sign = ""

        s = sign + s[::-1] 
        
        result = int(s)

        if result < -2 ** 31 or result >= 2 ** 31 or result == 0:
            return 0

        return result