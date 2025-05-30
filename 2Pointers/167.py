class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0
        r = len(numbers) - 1
        while l < r:
            L = numbers[l]
            R = numbers[r]
            candidate = L + R
            if candidate == target:
                return [l + 1, r + 1]
            if candidate < target:
                l += 1
            if candidate > target:
                r -= 1
        return "Answer not found."