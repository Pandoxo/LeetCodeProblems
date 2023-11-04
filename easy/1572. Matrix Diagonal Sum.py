class Solution(object):
    def diagonalSum(self, mat):
        result = 0
        n = len(mat)
        for i in range(n):
            result += mat[i][i] + mat[i][n-i-1]
        if n % 2 == 1:
            result -= mat[(n-1)/2][(n-1)/2]
        return result