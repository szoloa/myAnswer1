while 1:
    ph = int(input())
    if(ph == 7):
        print('中性')
        break
    if(ph<=7 & ph>1):
        print('酸性')
        break
    if(ph>=7 & ph<=14):
        print('碱性')
        break
    print('请重新输入')