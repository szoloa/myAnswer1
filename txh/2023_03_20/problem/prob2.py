# 利用for循环求正整数n的所有约数，即求所有能把n整除的数字
n = int(input())
for i in range(1,n+1):
    if(n % i == 0):
        print(i,end=' ')