class Solution(object):
    def move(self,position, direction, move):
        new_pos = [0,0]
        if move == "G":
            new_pos = [position[0] + direction[0], position[1] + direction[1]]
        elif move == "L":
            direction = [-direction[1], direction[0]]
            new_pos = position
        else:
            direction = [direction[1], -direction[0]]
            new_pos = position
        return new_pos, direction

    def isRobotBounded(self, instructions):
        if "G" not in instructions:
            return True
        pos = [0,0]
        dir = [0,1]
        for inst in instructions:
            result = Solution.move(self,pos, dir, inst)
            pos, dir = result[0], result[1]
        if pos == [0,0]:
            return True
        if dir != [0,1]:
            return True
        return False

## Could be shorter but idc