class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binstr = str(bin(N))[2:]
        dist = 0
        lastone = binstr.find('1')
        if lastone == -1:
            return 0
        for i in range(lastone + 1, len(binstr)):
            if binstr[i] == '1':
                if i - lastone > dist:
                    dist = i - lastone
                lastone = i
        return dist


s = Solution()
print(s.binaryGap(22))
print(s.binaryGap(1025))
print(__name__)