class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1 

        while low < high:
            mid = low + ((high - low) // 2)

            if nums[low] > nums[mid]:
                high = mid
            elif nums[high] < nums[mid]:
                low = mid + 1
            else:
                 return nums[low] 