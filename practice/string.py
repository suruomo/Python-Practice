
#访问字符串中的值
var1="hello world"
print(var1[0])
print(var1[1:5])
#更新字符串
print("更新字符串为：",var1[:6]+'woo')
#判断字符在不在字符串
if('e' in var1):
    print("e在字符串{}中".format(var1))
#格式化字符串
print ("My name is %s and weight is %d kg!" % ('Zara', 21))