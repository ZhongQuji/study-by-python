size = int(input("请输入棋盘的大小："))
for i in range(size):
    for j in range(size):
        if i == 0 and j == 0:
            print("┏",end='')
        elif i == 0 and j == size - 1:
            print("┓",end='')
        elif i == size - 1 and j == 0:
            print("┗",end='')
        elif i == size - 1 and j == size - 1:
            print("┛",end='')
        elif j == 0:
            print("┠",end='')
        elif i == size - 1:
            print("┷",end='')
        elif j == size - 1:
            print("┨",end='')
        elif i == 0:
            print("┯",end='')
        else:
            print("┼",end='')
    print('')