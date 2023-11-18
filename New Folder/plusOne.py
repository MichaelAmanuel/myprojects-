

class Solution(object):
    def plusOne(self, digits):
        sum = 0
        for i in digits:
            sum = sum * 10  + i
        total_sum = sum +1
        digits = []

        while total_sum != 0:
            dig = total_sum % 10
            digits.append(dig)
            total_sum = total_sum // 10
        digits.reverse()
        return (digits)
solution_instance = Solution()
digits = [4,3,2,1]
print(solution_instance.plusOne(digits))
























































