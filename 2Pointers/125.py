class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_s = [char.lower() for char in s if char.isalnum()]

        l = 0 
        r = len(cleaned_s) - 1
        while l < r:

            if cleaned_s[l] != cleaned_s[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True