class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val in nums:
            for i in range(nums.count(val)):
                nums.remove(val)


if __name__ == '__main__':
    print(Solution().removeElement(nums=[3, 2, 2, 3], val=3))
    print(Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
