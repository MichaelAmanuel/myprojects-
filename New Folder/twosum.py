# -*- coding: utf-8 -*-
"""twoSum.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q10RxreTNU6fNXB3XHo7o0ey38l7MUGR
"""

class Solution(object):
    def twoSum(self, numbers, target):
      o_p = []
      for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
          if (numbers[i] + numbers[j]) == target:
            o_p.append(i+1)
            o_p.append(j+1)

      return o_p

solution = Solution()
numbers = [0,0,3,4]
target = 0
print(solution.twoSum(numbers, target))

class Solution(object):
    def twoSum(self, numbers, target):
      o_p = []
      for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
          if (numbers[i] + numbers[j]) == target:
            o_p.append(numbers.index(numbers[i])+1)
            o_p.append(numbers.index(numbers[j])+1)

      return o_p

solution = Solution()
numbers = [0,0,3,4]
target = 0
print(solution.twoSum(numbers, target))