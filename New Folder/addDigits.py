
class Solution(object):
    def addDigits(self, num):
        num = str(num)
        while len(num) > 1:
            dig = int(num) % 10 + int(num) // 10
            num = str(dig)
            str(num)

        return num

solution_instance = Solution()
num = 38
result = solution_instance.addDigits(num)
print(result)














































































































