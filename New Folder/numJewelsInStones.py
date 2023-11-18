class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        jewels_len = len(jewels)
        for i in jewels:
            for j in stones:
                if i == j:
                    count += 1
        return count

solution_instance = Solution()
jewels = "z"
stones = "ZZ"
result = solution_instance.numJewelsInStones(jewels, stones)
print(result)
































