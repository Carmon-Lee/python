class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = bin(n)[2:].rjust(32, '0')
        reversed_bits = bits[::-1]
        return int(reversed_bits, 2)


if __name__ == '__main__':
    print(Solution().reverseBits(43261596))
