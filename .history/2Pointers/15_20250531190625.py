class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        seen = set()
        answer = []
        nums.sort()


        for i in range(len(nums) - 3):

            low = i + 1
            high = len(nums) - 1
            if nums[i] > 0:
                return answer
                
            if nums[i] in seen:
                continue
            else:

                while low < high:
                    res = nums[i] + nums[low] + nums[high]
                    if  res == 0:
                        answer.append((nums[i], nums[low], nums[high]))

                        while nums[high] == nums[high-1]:
                            high -= 1
                        while nums[low] == nums[low+1]:
                            low += 1

                    elif res < 0:
                        low += 1
                    elif res > 0:
                        high -= 1
        return answer



