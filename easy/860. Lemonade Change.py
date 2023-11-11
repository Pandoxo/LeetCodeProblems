class Solution(object):
    def lemonadeChange(self, bills):
        change = 0
        fives, tens = 0, 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                fives -= 1
            else:
                if tens > 0:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            if fives < 0:
                return False

        return True


ob = Solution()
print(ob.lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20]))
