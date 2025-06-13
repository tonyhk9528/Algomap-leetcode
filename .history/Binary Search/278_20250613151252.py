# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l = 0
        r = n - 1

        while l < r:
            mid = l + ((r - l) // 2)

            if isBadVersion(mid + 1):
                r = mid
            else:
                l = mid + 1
            
        return l + 1