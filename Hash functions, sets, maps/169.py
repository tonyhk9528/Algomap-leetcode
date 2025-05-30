class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        answer = -1
        count = 0

        for num in nums:
            if count == 0:
                answer = num
                count += 1
            elif num == answer:
                count += 1
            elif num != answer:
                count -= 1

        return answer 