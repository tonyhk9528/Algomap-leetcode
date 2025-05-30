class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        row_check = set()
        column_check = set()
        box1_check = set()
        box2_check = set()
        box3_check = set()

       
        for i  in range(9):
            for j in range(9):
                x = board[i][j]
                #check row
                if x in row_check and x != '.':
                    return False
                elif x != '.':
                    row_check.add(x)

                #check box
                if j < 3:
                    if (x in box1_check) and x != '.':
                        return False
                    elif x != '.':
                        box1_check.add(x)
                elif j < 6:
                    if (x in box2_check) and x != '.':
                        return False
                    elif x != '.':
                        box2_check.add(x)
                else:
                    if (x in box3_check) and x != '.':
                        return False
                    elif x != '.':
                        box3_check.add(x)
            
                #check column
                y = board[j][i]
                if y in column_check and y != '.':
                    return False
                elif y != '.':
                    column_check.add(y)

            row_check = set()
            column_check = set()

            if (i + 1) % 3 == 0:
                box1_check = set()
                box2_check = set()
                box3_check = set()

        return True
