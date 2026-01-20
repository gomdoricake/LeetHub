class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxWater = [0 for i in range(n)]
        
        # height = [1,8,6,2,5,4,8,3,7]
        # rank_idx = [0,3,7,5,4,2,8,1,6]
        for i in range(n):

            # from left
            pointer = 0
            while True: 
                if pointer >= i:
                    break
                if height[pointer] >= height[i]:
                    maxWater[i] = max(maxWater[i], (i - pointer) * height[i])
                    break
                pointer += 1

            # from right
            pointer = n-1
            while True: 
                if pointer <= i: 
                    break
                if height[pointer] >= height[i]: 
                    maxWater[i] = max(maxWater[i], (pointer - i) * height[i])
                    break   
                pointer -= 1

        return max(maxWater)