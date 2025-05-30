class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        answer = []

        while l < r:
            L = nums[l]**2
            R = nums[r]**2
            if L >= R:
                answer.append(L)
                l += 1
            else:
                answer.append(R)
                r -=1
        
        answer.append(nums[r]**2)
        
        answer.reverse()
        return answer