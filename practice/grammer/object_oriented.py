# 类的简单实例
class MyClass:
    i = 1234
    # 构造方法_init_()
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.z = imagpart

    def f(self):
        return "hello world"
# 创建类对象
b = MyClass(3.0,3.6)
print(b.r)
print(b.z)
print(b.f())
