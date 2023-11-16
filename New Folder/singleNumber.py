
class Solution(object):

    def singleNumber(self, nums):

        for i in nums:
            count = 0
            for j in nums:
                if i == j:
                    count = count + 1
            if count < 2:
                return i


solution_instance = Solution()
nums = [4]

print(solution_instance.singleNumber(nums))


























































