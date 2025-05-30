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
            direction = get_direction(current, i, j, matrix, answer, n, m)


    def get_direction(current, i, j, matrix, answer, n, m):
        change = False

        #check right
        if current == "right":
            if (j + 1 >= m) or (matrix[i][j+1] in answer):
                current = "down"
        
        if current == "down":
            if ((i + 1) >= n) or (matrix[i+1][j] in answer):
                change = True

        if current == "left":
            if ((j - 1) <= 0) or (matrix[i][j-1] in answer):
                change = True
        
        if current == "up":
            if ((i - 1) <= 0) or (matrix[i-1][j] in answer):
                change = True

        move(current, matrix, answer, i, j)


    def move(current, matrix, answer, i, j):

        if current == "right":
            j += 1
            answer.append(matrix[i][j])


        if current == "down":
            i += 1
            answer.append(matrix[i][j])

        if current == "left":
            j -= 1
            answer.append(matrix[i][j])

        if current == "up":
            i -= 1
            answer.append(matrix[i][j])





    












