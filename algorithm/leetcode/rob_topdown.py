class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {0: 0}
        return self.start_rob(nums, cache)

    def start_rob(self, arrs, cache):

        if len(arrs) <= 1:
            return sum(arrs)
        # if cache.get(len(arrs) - 2, None) is None:
        #     cache[len(arrs) - 2] = self.start_rob(arrs[:-2], cache)
        if cache.get(len(arrs) - 1, None) is None:
            cache[len(arrs) - 1] = self.start_rob(arrs[:-1], cache)
        cache[len(arrs)] = max(arrs[-1] + cache[len(arrs) - 2], cache[len(arrs) - 1])
        return cache[len(arrs)]


if __name__ == '__main__':
    print(Solution().rob([2, 7, 9, 3, 1]))
    print(Solution().rob([1, 2, 3, 1]))
