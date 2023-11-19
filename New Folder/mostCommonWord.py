# class Solution(object):
#
#     def mostCommonWord(self, paragraph, banned):
#         new_sent = []
#         count = 0
#         for i in paragraph.split(' '):
#             if i != banned:
#                 new_sent.append(i)
#
#         max_1 = 0
#         out_put = ""
#         for j in new_sent:
#             count = 0
#             for k in new_sent:
#                 if j == k:
#                     count += 1
#             if count > max_1:
#                 max_1 = count
#                 out_put = j
#
#         return out_put
#
#
# solution_instance = Solution()
#
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# # paragraph = "a."
# paragraph = paragraph.lower()
# paragraph = paragraph.replace(',', '').replace('.', '')
# banned = ["hit"]
# # paragraph = "a."
# # banned = []
# if len(banned) == 1:
#     banned = banned[0]
#     result = solution_instance.mostCommonWord(paragraph, banned)
# else:
#     result = solution_instance.mostCommonWord(paragraph, banned)
#
# print(result)















































































































