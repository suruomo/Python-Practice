list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print([3 * x for x in list2])
# 使用 append() 添加元素
list1.append('Google')
list1.append('Run')
# 迭代器
item = iter(list1)
while True:
    try:
        print(next(item))
    except StopIteration:
        break
# 删除元素
del list1[1]
print(list1)
print(max(list2))
# 遍历
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
