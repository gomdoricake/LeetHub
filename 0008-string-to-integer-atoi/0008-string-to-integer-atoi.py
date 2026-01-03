import re

class Solution:
    def myAtoi(self, s: str) -> int:
        
        idx, size, sign = 0, len(s), ''
        dig, letter = re.compile('[0-9]'), re.compile('[A-Z.a-z]')
        result = ''
        
        # skip whitespaces, initial zeros and set sign
        while True: 
            if idx >= size: break
            if letter.match(s[idx]): return 0

            if s[idx] == '+':
                idx += 1
                break
            elif s[idx] == '-': 
                sign = '-'
                idx += 1
                break
            elif not s[idx] == ' ' or dig.match(s[idx]): 
                break
            
            idx += 1
        
        while True: 
            if idx >= size: break
            if len(result) == 0 and letter.match(s[idx]): return 0
            if dig.match(s[idx]): result += s[idx]
            else: break

            idx += 1

        if len(result) == 0: return 0

        int_result = int(sign + result)

        if int_result < -2**31: return -2**31
        if int_result > 2**31 - 1: return 2**31 - 1
        return int(sign + result)