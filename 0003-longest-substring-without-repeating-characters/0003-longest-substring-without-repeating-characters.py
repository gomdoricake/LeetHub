class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        stat = 0
        result = 1
        size = len(s)

        if size == 0: 
            return 0

        for i in range(size): 
            
            for sub in range(stat, i):
                if s[sub] == s[i]: 
                    stat = sub + 1
                
            result = max(result, i - stat + 1)
        
        return result