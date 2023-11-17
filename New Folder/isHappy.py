

class Solution(object):

    def isHappy(self, n, max):
        num_str = str(n)
        sum = 0
        for i in range(0, len(num_str)):
            sum = sum + int(num_str[i]) ** 2
        max_loop = max
        if sum != 1:
            if max_loop == 0:
                print(False)
            else:
                max_loop -= 1
                self.isHappy(sum,max_loop)

        else:
            print(True)


solution_instance = Solution()
n = 19
max_loop = 990
solution_instance.isHappy(n, max_loop)


















































