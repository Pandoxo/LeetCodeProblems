class Solution(object):
    def checkStraightLine(self, coordinates):
        coordinates.sort()
        vec = [coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]]
        for i in range(len(coordinates) - 1):
            new_vec = [coordinates[i][0] + vec[0], coordinates[i][1] + vec[1]]
            if new_vec != coordinates[i+1]:
                return False
        return True


ob = Solution()
print(ob.checkStraightLine([[0,0],[0,1],[0,-1]]))
