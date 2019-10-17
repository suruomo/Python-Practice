# 继承
class People:
    name = ""
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    _gender = "女"


    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def says(self):
        print("我是{name}，性别{gender},今年{age}岁了".format(name=self.name,gender= self.gender, age=self.age))


class Student:
    grade = "一年级"

    def __init__(self, name, age, gender, grade):
        People.__init__(self, name, age, gender)
        self.grade = grade

    def says(self):
        print("我是{name}，性别{gender},今年{age}岁了,今年{grade}年级".format(name=self.name, gender=self.gender, age=self.age, grade=self.grade))


s = Student("Anna", 12, "女", "6")
s.says()
