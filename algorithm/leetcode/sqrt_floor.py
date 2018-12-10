import math


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        comp_digits = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

        comp_count = list(map(lambda x: s.count(x), comp_digits))
        for i in comp_digits:
            s = s.replace(i, '')
        single_count = list(map(lambda x: s.count(x), digits))
        product = zip([*comp_count, *single_count], [4, 9, 40, 90, 400, 900, 1, 5, 10, 50, 100, 500, 1000])
        return sum(map(lambda x: x[0] * x[1], product))


if __name__ == '__main__':
    print(Solution().romanToInt('IV'))
    print(Solution().romanToInt('III'))
    print(Solution().romanToInt('IV'))
    print(Solution().romanToInt('IV'))
    # print(Solution().hammingWeight(4))
    # print(Solution().hammingWeight(8))
    # print(Solution().hammingWeight(9))
    # print(Solution().hammingWeight(13))
