num = int(input())
sum = 1
for i in range(1,num+1):
    cj = 1
    for j in range(1,i+1):
        cj *= j
    sum += 1/cj
print('当n={}时，e的近似值为{}'.format(num,sum))