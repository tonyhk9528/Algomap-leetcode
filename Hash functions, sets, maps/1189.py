class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = 0

        balloon_dict = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}

        for c in text:
            if c in balloon_dict:
                balloon_dict[c] += 1

        while True:
            for k, v in balloon_dict.items():
                if k in ('b', 'a', 'n'):
                    if v < 1:
                        return count
                    else:
                         balloon_dict[k] -= 1
                elif k in ('l', 'o'):
                    if v < 2:
                        return count
                    else:
                        balloon_dict[k] -= 2
            count += 1