class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        l = 0 
        n = len(s2)
        k = len(s1)

        if k > n:
            return False
        
        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(k):
            freq1[ord(s1[i]) - 97] += 1
            freq2[ord(s2[i]) - 97] += 1
        
        if freq1 == freq2:
            return True


        for i in range(k, n):
            freq2[ord(s2[l]) - 97] -= 1
            freq2[ord(s2[i]) - 97] += 1
            if freq1 == freq2:
                return True
            
            l += 1
        
        return False
