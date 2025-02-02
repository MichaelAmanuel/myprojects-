# -*- coding: utf-8 -*-
"""check

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19590nUeYrPa7so5J0zjWB7OKAA9eMkyU
"""

class Solution(object):
    def check(self, nums):
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        return count <= 1

sol = Solution()
print(sol.check([3, 4, 5, 1, 2]))  # True
print(sol.check([2, 1, 3, 4]))  # False
print(sol.check([1, 2, 3]))  # True
print(sol.check([1, 1, 1, 1]))  # True
print(sol.check([4, 5, 6, 7, 1, 2, 3]))  # True

class Solution(object):
    def check(self, nums):

      ni = min(nums)
      if nums[0] != ni:
        for i in range(nums.index(ni), len(nums)-1):
          if nums[i] > nums[i+1]:
            return False

        for i in range(nums.index(ni)):
          if nums[i - 1] > nums[i]:
            return False

      else:
        if nums[0] != nums[len(nums)-1]:
          for i in range(nums.index(ni), len(nums)-1):
            if nums[i] > nums[i+1]:
              return False
        else:
          for i in range(len(nums)-1):
            if nums[i - 1] > nums[i]:
              return False

      return True

solution = Solution()
nums = [6,10,6]
print(solution.check(nums))