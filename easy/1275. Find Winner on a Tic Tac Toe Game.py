class Solution(object):
    def tictactoe(self, moves):
        grid = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]
        count = 1

        player = "A"
        for move in moves:
            if count % 2 == 0:
                player = "B"
            else:
                player = "A"
            grid[move[0]][move[1]] = player

            right = 0
            for row in range(3):
                for column in range(3):
                    if grid[row][column] != player:
                        break
                    else:
                        right +=1
                if right == 3:
                    return player
                right = 0

            for column in range(3):
                for row in range(3):
                    if grid[row][column] == player:
                        right += 1
                if right == 3:
                    return player
                right = 0

            for i in range(3):
                if grid[i][i] == player:
                    right += 1
            if right == 3:
                return player
            right = 0

            for j in range(3):
                if grid[j][2-j] == player:
                    right += 1
            if right == 3:
                return player

            if count == 9:
                return "Draw"
            count += 1

        return "Pending"

ob = Solution()
print(ob.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))