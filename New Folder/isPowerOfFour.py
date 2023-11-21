class Solution(object):
    def isPowerOfThree(self, n):
        i = 0
        while  3 ** i <= n:
            if  3 ** i == n :
                return True
            i += 1
        else:
            return False

solution_instance = Solution()
n = 43046722
result = solution_instance.isPowerOfThree(n)
print(result)











































































































