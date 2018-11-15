import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc,logfbank

# sampling_freq,audio=wavfile.read('')


import re
# 将t替换为b，同时去掉结尾的_1_
string1 = 'note_x5F_t_x5F_133_1_,note_x5F_t_x5F_133_1_,note_x5F_t_x5F_133_1_,'
# 目标的正则表达式
target = r'(.*?)(\d{3})_1_'
# 结果的正则表达式
result = r'\1\2'
# 使用sub全部替换
s1 = re.sub(target, result, string1)
print(s1)


def unwrap(*args):
    print(args)

if __name__ == '__main__':
    a='发动机啊了'
    print(a)

