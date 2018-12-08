class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        last_char, last_count = '', 0
        char_set = []
        for i in chars:
            if i != last_char:
                char_set.append(last_char)
                if last_count > 1:
                    char_set.append(str(last_count))
                last_char = i
                last_count = 1
            else:
                last_count += 1
        print(char_set)
        char_set.append(last_char)
        if last_count > 1:
            char_set.append(str(last_count))

        new_chars=''.join(char_set)

        print(new_chars)
        for i in range(len(new_chars)):
            chars[i] = new_chars[i]
        return len(new_chars)


if __name__ == '__main__':
    # data = ["a", "b", "b", "c", "c", "c", 'a', 'a']
    data = ["a", "b", "c", "c", "c", 'a', 'a']
    result = Solution().compress(data)
    for i in range(result):
        print(data[i])
