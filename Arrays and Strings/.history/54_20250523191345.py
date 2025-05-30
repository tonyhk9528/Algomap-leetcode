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
        current = "right"

        answer = []

        while s != l :
            answer.append(matrix[i][j])
            direction = get_direction(i, j, matrix)


    def get_direction(current, i, j, matrix, answer, n, m):
        change = False

        #check right
        if current == "right":
            if (j + 1 >= m) or :
                change = True
            else:
                j += 1
                answer.append(matrix[i][j])
        

        if current == "down":
            if j + 1 >= m:
                change = True
            else:
                j += 1
                answer.append(matrix[i][j])

        



        if change:













