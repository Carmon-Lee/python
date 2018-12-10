class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = sorted(g), sorted(s)
        print(g, s)
        res_count = 0
        si = 0
        for i in range(len(g)):
            while si < len(s) and s[si] < g[i]:
                si += 1
            if len(s) == si:
                break
            res_count += 1
            si += 1
        return res_count


if __name__ == '__main__':
    # print(Solution().findContentChildren([1, 2, 3], [1, 1]))
    print(Solution().findContentChildren([1, 2, 3], [3]))
