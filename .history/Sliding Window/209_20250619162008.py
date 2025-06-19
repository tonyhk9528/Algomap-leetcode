class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        min_l = n + 1
        sum = 0

        for r in range(n):
            sum += nums[r]

            while sum >= target:
                min_l = min(min_l, r - l + 1)
                sum -= nums[l]
                l += 1
        if min_l != n + 1:
            return min_l
        else:
            return 0