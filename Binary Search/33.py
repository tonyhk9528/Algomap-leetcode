class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        def find_m():
            low, high = 0, len(nums) - 1
            while low < high:
                mid = (low + high) // 2
                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid
            return low

        def binary_search(low, high):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        n = len(nums)
        m = find_m()

        if nums[m] <= target <= nums[n - 1]:
            return binary_search(m, n - 1)
        else:
            return binary_search(0, m)
