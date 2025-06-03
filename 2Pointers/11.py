class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(height) - 1

        answer = 0

        while l < r:
            amount = min(height[l], height[r]) * (r - l) 
            if amount > answer:
                answer = amount
            
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        
        return answer
