class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        n = len(matrix[0])
        L = m * n

        low = 0
        high = L - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            if matrix[mid // n][mid % n] == target:
                return True

            elif matrix[mid // n][mid % n] < target:
                low = mid + 1
            
            else:
                high = mid - 1
        
        return False
