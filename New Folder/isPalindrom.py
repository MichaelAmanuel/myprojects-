


class Solution(object):
    def isPalindrome(self, Input):
        input_1 = ''
        for i in Input:
            if i.isalpha():
                input_1 += i.lower()
        if len(input_1) <= 1:
            return False
        for i, j in zip(input_1, reversed(input_1)):
            if i != j:
                return False
        else:
            return True

solution_instance = Solution()
s = "0P"
print(solution_instance.isPalindrome(s))























































