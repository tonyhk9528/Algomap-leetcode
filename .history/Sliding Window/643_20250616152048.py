class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        total = sum(nums[:k])
        answer = total

        for i in range(k, len(nums)):
            total += nums[i] - nums[i - k]
            answer = max (answer, total)

        return answer / float(k)