# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/5/3 13:47'
# 问题455

def find(g,s):
    if g==None and s==None:
        return 0
    g.sort()
    s.sort()
    i=0
    j=0
    while i< len(g) and j<len(s):
        if g[i]<=s[j]:
            i=i+1
        j=j+1
    print(i)


g=[1,2,3]
s=[1,1]
find(g,s)
