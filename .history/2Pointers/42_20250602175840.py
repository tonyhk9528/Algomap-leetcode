class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_l = 0
        max_r = 0
        L = []
        R = []
        water = 0

        for i in range(len(height)):
            L.append(max_l)
            max_l = max(max_l, height[i])
            
            R.append(max_r)
            max_r = max(max_r, height[len(height) - 1 -i])

        R.reverse()

        for i in range(len(L)):
            water += max((min(L[i], R[i]) - height[i]), 0) 
        
        return water