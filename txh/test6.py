num = int(input())
if(num%3 == 0 & num%5==0 & num%7==0):
    print('{}无法同时被3、5、7整除'.format(num))
