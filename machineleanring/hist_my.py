class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        bits = {'0': 0, '1': 1}
        max_len = max(len(a), len(b))
        carry = 0
        output = []
        a, b = a.rjust(max_len, '0'), b.rjust(max_len, '0')
        for i, j in zip(a[::-1], b[::-1]):
            carry, rem = divmod(bits[i] + bits[j] + carry, 2)
            output.append(str(rem))
        if carry > 0:
            output.append(str(carry))
        return ''.join(output)[::-1]


if __name__ == '__main__':
    print(Solution().addBinary("1111", "1111"))
    # print(Solution().searchInsert([1, 3, 5, 6], 2))
    # print(Solution().searchInsert([1, 3, 5, 6], 7))
