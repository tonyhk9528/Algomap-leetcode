class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check = {}

        for i in range(len(nums)):
            if nums[i] in check:
                return [check[nums[i]], i]
            else:
                diff = target - nums[i]
                check[diff] = i