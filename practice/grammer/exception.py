# 简单示例
# while True:
#     try:
#         x = int(input("输入一个整数："))
#         break
#     except ValueError:
#         print("无效数字，请重新输入")
# 抛出异常
# raise NameError('HiThere')
# 捕获多个异常
# try:
#     f = open('F://python_test.txt')
#     s = f.readline()
#     i = int(s.strip())
#
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# else:  # else放在最后，没有任何异常时执行
#     print(f.name, 'has', len(f.readlines()), 'lines')
#     f.close()
# 用户自定义异常
class MyError(Exception):
    def _int_(self, value):
        self.value = value

    def _str_(self):
        return repr(self.value)
try:
    raise MyError(2 * 3)
except MyError as e:
    print("产生异常，值：", e.value)
