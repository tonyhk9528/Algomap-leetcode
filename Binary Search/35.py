class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = low + ((high-low) // 2)

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1
            
            elif nums[mid] > target:
                high = mid - 1
        
        return low
