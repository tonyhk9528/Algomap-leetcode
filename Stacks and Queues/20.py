class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        check = {"(":")", "[":"]", "{":"}"}

        for symbol in s:
            if symbol in check:
                stack.append(check[symbol])
            elif stack:
                if symbol != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                return False

        return stack == []   
