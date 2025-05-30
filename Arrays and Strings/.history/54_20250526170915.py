class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        answer = []
        visited = []
        i = 0
        j = 0
        UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
        m = len(matrix)
        n = len(matrix[0])
        l = m*n
        direction = RIGHT

        answer.append(matrix[i][j])

        while len(answer) < l:
            if direction == RIGHT:
                if (j+1 < n) and (i,j+1) not in visited:
                    j += 1
                    answer.append(matrix[i][j])
                    visited.append((i,j))
                else:
                    direction = DOWN
            elif direction == DOWN:
                if (i + 1 < m ) and (i+1,j) not in visited:
                    i += 1
                    answer.append(matrix[i][j])
                    visited.append((i,j))
                else:
                    direction = LEFT
            if direction == LEFT:
                if (j-1 >= 0) and (i, j-1) not in visited:
                    j -= 1
                    answer.append(matrix[i][j])
                    visited.append((i,j))
                else:
                    direction = UP
            if direction == UP:
                if (i - 1 >= 0) and (i - 1, j) not in visited:
                    i -= 1
                    answer.append(matrix[i][j])
                    visited.append((i,j))
                else:
                    direction = RIGHT








    












