
class Solution:

    def addTwoNumbers(self, l1, l2):
        i = len(l1) - 1
        st1 = 0
        out = []
        if len(l1) == len(l2):
            st1 = 0
            i = len(l1)-1
            while i >= 0:
                st1 = st1 * 10 + l1[i] + l2[i]
                i = i - 1
            stri = str(st1)
            for i in reversed(stri):
                out.append(int(i))
            print(out)

        else:
            st2 = 0
            j = len(l2) - 1
            while i >= 0:
                st1 = st1 * 10 + l1[i]
                i = i - 1

            while j >= 0:
                st2 = st2 * 10 + l2[j]
                j = j - 1

            stri = str(st1 + st2)

            for i in reversed(stri):
                out.append(int(i))
            print(out)

solution_instance = Solution()
l1 = [2,4,3]
l2 = [5,6,4]

solution_instance.addTwoNumbers(l1, l2)









