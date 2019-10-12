# 默认参数
def printinfo(name, age=29):
    print("name:", name)
    print("age:", age)
    return
printinfo("And", 34)
printinfo("Bob")
# 不定长参数:*以元组形式返回,**字典形式返回
def printinfos(arg1,*vartuple):
    print("输出：")
    print(arg1)
    print(vartuple)

def printdicts(arg1, **vartuple):
    print("输出：")
    print(arg1)
    print(vartuple)

printinfos(70,34,232,22,1,23)
printdicts(70,s=232,v=1)

# Lambda表达式
sum=lambda a,b:a+b
print("相加后的值是：",sum(1,4))
