class Solution(object):
    def calPoints(self, operations):
        result = []
        for i in range(len(operations)):
            if operations[i] == "C":
                result.pop()
            elif operations[i] == "D":
                result.append((result[-1])*2)
            elif operations[i] == "+":
                result.append(result[-1] + result[-2])
            else:
                result.append(int(operations[i]))
        return sum(result)

ob = Solution()
print(ob.calPoints(["5","-2","4","C","D","9","+","+"]))