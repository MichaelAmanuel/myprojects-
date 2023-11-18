
class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for i in operations:
            if i == "--X" or i == "X--":
                x += -1
            else:
                x += 1
        print(x)

solution_instance = Solution()
operations = ["X++","++X","--X","X--"]
solution_instance.finalValueAfterOperations(operations)












































