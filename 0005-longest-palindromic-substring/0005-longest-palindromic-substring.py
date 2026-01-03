class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        size = len(s)
        str_size = 0
        max_left = 0
        max_right = 0

        if size == 1 or size == 2 and s[0] == s[1]: 
            return s

        for target_ptr in range(1, size - 1):
            left_ptr = target_ptr - 1
            right_ptr = target_ptr + 1

            if s[left_ptr] == s[target_ptr]: 
                right_ptr = left_ptr + 1
                
            elif s[right_ptr] == s[target_ptr]:
                left_ptr = target_ptr


            # if same letter continues
            while left_ptr - 1 >= 0 and s[left_ptr - 1] == s[target_ptr] and s[left_ptr] == s[target_ptr]: 
                left_ptr -= 1

            while right_ptr + 1 < size and s[right_ptr + 1] == s[target_ptr] and s[right_ptr] == s[target_ptr]: 
                right_ptr += 1

            while True: 
                if left_ptr < 0 or right_ptr >= size: break
                
                if s[left_ptr] != s[right_ptr]: break

                if right_ptr - left_ptr + 1 > str_size: 
                    str_size = right_ptr - left_ptr + 1
                    max_left = left_ptr
                    max_right = right_ptr
                
                left_ptr -= 1
                right_ptr += 1    

        result = ""

        for c in range(max_left, max_right + 1): 
            result += s[c]
        
        return result