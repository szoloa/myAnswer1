# 输出100-200之间不能被3整除的数，每行输出8个
j = 0
for i in range(99, 200):
    if(j == 8):
        j = 0
        print()
    if(i % 3 != 0):
        print(i, end=' ')
        j += 1