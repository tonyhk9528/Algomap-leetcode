class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        answer = 0

        count = {}
        for stone in stones:
            if stone in count:
                count[stone] += 1
            else:
                count[stone] = 1
        
        for jewel in jewels:
            if jewel in count:
                answer += count[jewel]

        return answer 