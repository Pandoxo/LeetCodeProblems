class Solution(object):
    def printVertical(self, start, end, column, matrix):
        for i in range(start, end):
            print(matrix[i][column])
    def printHorizontal(self, start, end, row, matrix):
        for i in range(start, end):
            print(matrix[row][i])

    def spiralOrder(self, matrix):
        min_row = 0
        min_col = 0
        max_row = 0
        max_col = 0
        rows = len(matrix)
        cols = len(matrix[0])
        cels = rows * cols

        prVertical = False



ob = Solution()
ob.printHorizontal(0, 3, 2,
                 [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
