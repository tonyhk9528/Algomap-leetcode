class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(nums)
        l = 0
        max_w = 0
        number_zero = 0
        
        for r in range(n):
            if nums[r] == 0:
                number_zero += 1
            
            while number_zero > k:
                if nums[l] == 0:
                    number_zero -= 1
                l += 1

            max_w = max( max_w, (r - l + 1) )
        
        return max_w