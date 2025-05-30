class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        answer = 0
        length = 0
        check = set(nums)

        for num in check:
            if num - 1 not in check: #start a sequence 
                length += 1
                while num + i in check:
                    length += 1
                    i += 1
                if length > answer:
                    answer = length
                length = 0
                i = 1
        return answer