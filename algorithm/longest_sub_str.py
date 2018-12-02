import random
import time


def decode_hoffman():
    decoded_file = ''
    cur_str = lines
    while cur_str:
        for code in codes:
            if cur_str.startswith(code):
                decoded_file += code
                cur_str = cur_str[len(code):]
        # cur_str = cur_str[3:]
    return decoded_file


if __name__ == '__main__':
    codes = ['0', '100', '101', '110', '1110', '1111']

    lines = ''
    for i in range(500000):
        lines += codes[random.randint(0, 5)]
    # with open('file.txt', 'r') as f:
    #     lines = ''.join(f.readlines())
    print(lines)
    t1 = time.time()

    decoded_file = decode_hoffman()
    t2 = time.time()
    print(t2 - t1)
    print(decoded_file)
