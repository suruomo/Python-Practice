f=open("F://python_test.txt","a+")
f.write(input("请输入：")+"\n")
f=open("F://python_test.txt","r")
print(f.readline())
f.close()

with open("F://python_test.txt","r+") as f:
    r=f.read()
f.closed