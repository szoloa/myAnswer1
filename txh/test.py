(a,b) = (int(input()),int(input()))

for i in range(a-1,b):
    if(str(i)[::-1] == str(i)):
        print(i,end=',')