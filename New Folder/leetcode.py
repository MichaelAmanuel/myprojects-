class Solution:

    def twoSum(self, nums, target):
        list = []
        for i in nums:
            for j in range(1, len(nums)):
                if i + nums[j] == target and nums.index(i) != j :
                    x = nums.index(i)
                    if x not in list:
                        list.append(x)
                    if j not in list:
                        list.append(j)
        return list

solution_instance = Solution()

nums = [-1,-2,-3,-4,-5]
target = -8
result = solution_instance.twoSum(nums, target)
print(result)



# nums_two = [3,2,4]
# target_two = 6
# print(twoSum(nums_two, target_two))
#
# nums_3 = [3,3]
# target_3 = 6
# print(twoSum(nums_3, target_3))











