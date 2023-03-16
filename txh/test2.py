num = int(input())
sum = 0
for i in range(1,num+1):
    sum += 1/i
print('当n为{}时分式和为{}'.format(num,sum))