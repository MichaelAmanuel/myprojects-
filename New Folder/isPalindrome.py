

class Solution(object):
    def isPalindrome(self, x):

        y = str(x)
        for i, j in zip(y, range(len(y) - 1, -1, -1)):
            if i != y[j]:
                print(False)
                break
        else:
            print(True)

solution_instance = Solution()
x = 121

solution_instance.isPalindrome(x)







