
class Solution(object):
    def defangIPaddr(self, address):
        add = address.split('.')
        out_put = '[.]'.join(add)

        return str(out_put)

solution_instance = Solution()
address = "1.1.1.1"
result = solution_instance.defangIPaddr(address)
print(result)



























