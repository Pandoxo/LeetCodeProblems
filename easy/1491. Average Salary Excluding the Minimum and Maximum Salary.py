class Solution(object):
    def average(self, salary):
        min_salary = min(salary)
        max_salary = max(salary)
        total = sum(salary) - min_salary - max_salary
        return float(total) / (len(salary)-2)


ob = Solution()
print(ob.average([48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]))