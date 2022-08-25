# 计算器可以进行基础运算（加、减、乘、除）被除数不为0
first = float(input("请输入第一个数："))
second = float(input("请输入第二个数："))
operator = input("请选择运算符：+ - * /:")
if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    if second == 0:
        print("除数不能为0")
    else:
        print(first / second)
