str = 'Orange' # input()

for i in range(0,len(str)+1):
    print(str[i:],'X',str[len(str)-i:],sep='')