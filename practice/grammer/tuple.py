#元组不能修改元素值
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
tup4 = (50,)  #元组中只包含一个元素时，需要在元素后面添加逗号
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
tup3 = tup1 + tup2
print (tup3)