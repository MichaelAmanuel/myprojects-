
class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.split(" ")
        for i in range(len(word)-1, -1, -1):
            if word[i] != "":
                return (len(word[i]))


solution_instance = Solution()
s = "   fly me   to   the moon  "
result = solution_instance.lengthOfLastWord(s)
print(result)




















