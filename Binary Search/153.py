class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        low = 0
        high = n - 1 

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[low] > nums[mid]:
                high = mid
            elif nums[high] < nums[mid]:
                low = mid + 1
            else:
                 return nums[low] 
        return nums[low]