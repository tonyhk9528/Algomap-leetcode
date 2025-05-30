class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        answer = []
        check = {}

        

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in check:
                check[sorted_word] = [word]
            else:
                check[sorted_word].append(word)
        
        for k, v in check.items():
            answer.append(v)

        return answer