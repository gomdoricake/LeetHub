class Solution:
    def convert(self, s: str, numRows: int) -> str:
        size = len(s)
        result = ""

        if numRows == 1: return s

        for i in range(1, numRows + 1): 
            isEven = False
            prev = i - 1
            if prev >= size:
                result += ""
            else: 
                result += s[prev]
            
            while True: 
                isEven = not isEven
                if i == 1 or isEven and i != numRows:
                    nex = prev + 2*numRows - 2*i
                else: 
                    nex = prev + 2*numRows - 2*(numRows-i+1)
                
                if nex >= size: break

                result += s[nex]
                prev = nex
        
        return result