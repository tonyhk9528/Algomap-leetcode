import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def k_works(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/float(k))
            
            return hours <= h


        piles.sort()
        
        max_k = piles[len(piles) - 1]

        l = 1
        r = max_k

        while l < r:
            mid = l + ((r - l) // 2)
            if k_works(mid):
                r = mid
            else:
                l = mid + 1
        
        return l