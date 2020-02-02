# 小型学生管理系统
# 学生初始数据
data = [
    {
        'name': 'Tom',
        'sex': '女',
        'address': '西安'
    },
    {
        'name': 'Bob',
        'sex': '男',
        'address': '北京'
    },
    {
        'name': 'Cindy',
        'sex': '女',
        'address': '广州'
    }
]


# 1.显示所有学生信息
def show_all():
    for student in data:
        print(student)


# 2.新建学生信息
def create_student():
    name = input('输入名字：')
    sex = input('输入性别：')
    address = input('输入地址：')
    student = {
        'name': name,
        'sex': sex,
        'address': address
    }
    data.append(student)


# 3.查询学生信息
def find_student():
    name = input('请输入要查找学生姓名：')
    for student in data:
        if student['name'] == name:
            print(student)


# 4.修改学生信息
def modify_student():
    modify_name = input('请输入要修改学生姓名：')
    for student in data:
        if student['name'] == modify_name:
            student['name'] = input('修改名字：')
            student['sex'] = input('修改性别：')
            student['address'] = input('修改地址：')
    # 5.删除学生信息
def delete_student():
    modify_name = input('请输入要删除学生姓名：')
    for student in data:
        if student['name'] == modify_name:
            data.remove(student)

while True:
    print(
        """
        ************************
        欢迎使用【学生管理系统】V1.0
        1.显示所有学生信息
        2.新建学生信息
        3.查询学生信息
        4.修改学生信息
        5.删除学生信息
        6.退出系统
        ************************
        """
    )
    op = input("请输入操作序号:")
    if op == '1':
        show_all()
    elif op == '2':
        create_student()
    elif op == '3':
        find_student()
    elif op == '4':
        modify_student()
    elif op == '5':
        delete_student()
    elif op == '6':
        print('退出系统!\n')
        break
