class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(1000):
            if n == 1 or n == 4:
                break
            n = self.next_number(n)
            print(n)
        return n == 1

    def next_number(self, n):
        digits = []
        while n > 0:
            n, digit = divmod(n, 10)
            digits.append(digit)
        next_num = sum(map(lambda x: x ** 2, digits))
        return next_num


if __name__ == '__main__':
    # print(Solution().isHappy(20))
    print(Solution().isHappy(145))
    # s = Solution()
    # for i in range(1000):
    #     print('result of number {0} is {1}'.format(i, s.isHappy(i)))
    # print(Solution().isHappy(9999))
