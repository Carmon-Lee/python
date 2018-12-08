import random
import time


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def ensure_node(self, val):
        if val == '0':
            if not self.left:
                self.left = TreeNode('0')
        else:
            if not self.right:
                self.right = TreeNode('1')

    def get_next(self, letter):
        if letter == '0':
            return self.left
        else:
            return self.right


def decode_hoffman():
    decoded_file = ''

    node = root
    for i in lines:
        node = node.get_next(i)
        if not node.left and not node.right:
            decoded_file += node.val
            node = root
    # while cur_str:

    # for code in codes:
    #     if cur_str.startswith(code):
    #         decoded_file += code
    #         cur_str = cur_str[len(code):]
    # with open('output.txt','w') as f:
    #     f.writelines(lines)
    #     f.write('\n')
    #     f.writelines(decoded_file)
    return decoded_file


if __name__ == '__main__':
    codes = ['0', '100', '101', '110', '1110', '1111']
    code_book = {'0': 'a', '100': 'b', '101': 'c', '110': 'd', '1110': 'e', 'f': '1111'}

    root = TreeNode('root')
    cur_node = root

    for code in codes:
        cur_node = root
        for letter in code:
            cur_node.ensure_node(letter)
            cur_node = cur_node.get_next(letter)
        cur_node.val = code
    lines = ''
    t0 = time.time()

    for i in range(4000000):
        lines += codes[random.randint(0, 5)]
    # with open('file.txt', 'r') as f:
    #     lines = ''.join(f.readlines())
    # print(lines)
    t1 = time.time()
    print(t1 - t0)
    decoded_file = decode_hoffman()
    t2 = time.time()
    print(t2 - t1)
    # print(decoded_file)
