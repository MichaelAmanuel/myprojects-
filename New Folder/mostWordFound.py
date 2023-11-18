
class Solution(object):
    def mostWordsFound(self, sentences):
        max_len = 0
        for i in sentences:
            word = i.split(" ")
            if len(word) > max_len:
                max_len = len(word)
        return (max_len)

solution_instance = Solution()
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

result = solution_instance.mostWordsFound(sentences)
print(result)








































