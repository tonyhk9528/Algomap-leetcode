class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_l = 0
        n = len(s)
        seen = set()
        l = 0

        for r in range(n):
            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            max_l = max(max_l, (r - l + 1))
        
        return max_l