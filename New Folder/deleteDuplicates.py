
head = [1,1,2, 3, 3]
class Solution(object):
    def deleteDuplicates(self, head):
        for i in head:
            count = 0
            for j in head:
                if i == j:
                    count += 1
            if count >1:
                head.remove(i)

        return head

solution_instance = Solution()
head = [1,1,2, 3, 3]
result = solution_instance.deleteDuplicates(head)
print(result)













































































































