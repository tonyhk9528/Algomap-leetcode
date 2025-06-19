class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_l = 0
        letters = [0] * 26
        n = len(s)
        l = 0

        for r in range(n):
            letters[ord(s[r]) - 65] += 1

            while (r - l + 1) - max(letters) > k:
                letters[ord(s[l]) - 65] -= 1
                l += 1

            max_l = max (max_l, (r - l) + 1)  
        
        return max_l
