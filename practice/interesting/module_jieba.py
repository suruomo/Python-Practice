# 能够将一段中文文本分割成中文词语的序列

import jieba

s = jieba.lcut('能够将一段中文文本分割成中文词与的序列')
print(s)
