class Solution(object):
    def judgeCircle(self, moves):
        U = moves.count("U")
        D = moves.count("D")
        R = moves.count("R")
        L = moves.count("L")

        return R - L == 0 and U - D == 0