class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        l = 0
        r = l + k - 1
        answer = float('-inf')
        sum = 0
        while r < len(nums):
            for num in nums[l:r+1]:
               sum += num
            answer = max(answer, sum/float(k))
            sum = 0
            l += 1
            r += 1

        return answer 