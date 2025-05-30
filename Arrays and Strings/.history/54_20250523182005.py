class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = matrix.len()
        m = matrix[0].len
        l = n * m 
        i = 0
        j = 0
        s = 0

        answer = []

        while s != l :
            answer.append(matrix[i][j])
            




