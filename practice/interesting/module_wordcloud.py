# 生成词云图片
import jieba
from wordcloud import WordCloud
s="""
奇奇
果果
嘟嘟
跳跳
跳跳
跳跳
跳跳
欢欢
张苗雨
"""

cut_list=jieba.lcut(s)
new_str=' '.join(cut_list)#用空格重新拼接成一个字符串
word_cloud=WordCloud(font_path='msyh.ttc').generate(new_str)
word_cloud.to_file('词云.jpg')
