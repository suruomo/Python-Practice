import math
print(2**3)
s="Hello World"
print(str(s))
# 输出格式化
a="Amy"
b="Bob"
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
print(f'{a} 和 {b}')
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
   print('{0:10} ==> {1:10d}'.format(name, number))