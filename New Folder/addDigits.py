
# class Solution(object):
#     def addDigits(self, num):
#         num = str(num)
#         while len(num) > 1:
#             dig = int(num) % 10 + int(num) // 10
#             num = str(dig)
#             str(num)
#
#         return num
#
# solution_instance = Solution()
# num = 38
# result = solution_instance.addDigits(num)
# print(result)

# class Solution(object):
#
#     def myPow(self, x, n):
#         return x ** n
#
# solution_instance = Solution()
# x = 2.00000
# n = 10
# result = solution_instance.myPow(x, n)
#
# print(result)


# class Solution(object):
#
#     def superPow(self, a, b):
#         sum_out = ''
#         if len(b) == 1:
#             return a ** b[0]
#         for i in b:
#             sum_out = sum_out + str(i)
#         resu = a ** int(sum_out)
#         print(type(resu))
#         return resu
#
#
# solution_instance = Solution()
# a = 2
# b = [1, 0]
# result = solution_instance.superPow(a, b)
# print(result)

#
# class Solution(object):
#
#     def checkPerfectNumber(self, n):
#         sum_div = 0
#         for i in range(1, (num // 2) + 1):
#             if num % i == 0:
#                 sum_div += i
#         if sum_div == num:
#             print(True)
#         else:
#             print(False)
#
#         # return True if sum_div == num else False
#
#
# solution_instance = Solution()
# num = 99999991
# solution_instance.checkPerfectNumber(num)
# # print(result)

# n = 100
# out_put = ''
# while n != 0:
#     dig = n % 7
#     out_put = str(dig) + out_put
#     n = n // 7
#
# print(out_put)

# s = "a-bC-dEf-ghIj"
# d = ''
#
# for i, j in zip(range(len(s)-1, -1, -1), s):
#     if j == '-':
#         d = d + j
#         if s[i] != '-':
#             d = d + s[i]
#     else:
#         d = d + s[i]
#
# print(d)
#
# "j-Ih-gfE-dCba"


# nums = [-1,0,3,5,9,12]
# target = 2
# class Solution(object):
#     def search(self, nums, target):
#
#         for i in nums:
#             if i == target:
#                 return nums.index(i)
#         return -1
#
# solution = Solution()
# nums = [-1, 0, 3, 5, 9, 12]
# target = 9
# result = solution.search(nums, target)
# print(result)


# class Solution(object):
#     def hasGroupsSizeX(self, deck):
#
#         if len(deck) % 2 != 0:
#             return False
#         for i in deck:
#             count = 0
#             for j in deck:
#                 if i == j:
#                     count += 1
#             if count != 2:
#                 return False
#         return True
#
# solution = Solution()
# deck = [1]
# result = solution.hasGroupsSizeX(deck)
# print(result)
class Solution(object):
    def fib(self, n):
        a, b = 0, 1
        if n == 0:
            return a
        elif n == 1:
            return b
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c

        return c

solution = Solution()
n = 1
result = solution.fib(n)
print(result)





































































