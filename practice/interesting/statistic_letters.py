# coding=utf-8
import re
from collections import Counter


# 替换除了n't这类连字符外的所有非单词字符和数字字符
def replace(s):
    if s.group(1) == 'n\'t':
        return s.group(1)
    return ' '


def cal(filename='text.txt'):
    with open(filename, 'r') as f:
        data = f.read()
    data = data.lower()
    # 替换除了n't这类连字符外的所有非单词字符和数字字符
    data = re.sub(r'(n[\']t)|([\W\d])', replace, data)
    datalist = re.split(r'[\s\n]+', data)
    # collection中的Counter作用是：定义一个list数组，求数组中每个元素出现的次数
    return Counter(datalist).most_common()


if __name__ == '__main__':
    dic = cal()
    for i in range(len(dic)):
        print('%15s  ---->   %3s' % (dic[i][0], dic[i][1]))