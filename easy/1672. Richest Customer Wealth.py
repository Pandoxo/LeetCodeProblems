class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for customer in accounts:
            wealth = 0
            for bank in customer:
               wealth += bank
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth