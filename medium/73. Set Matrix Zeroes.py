class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        zeros = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zeros.append([row, col])
        for zero in zeros:
            for row in range(rows):
                matrix[row][zero[1]] = 0
            for col in range(cols):
                matrix[zero[0]][col] = 0
        return matrix


ob = Solution()
print(ob.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
