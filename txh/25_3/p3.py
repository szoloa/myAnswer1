x = int(input())
e = 0.001
g = x/2
while 1:
    if(abs(g*g-x)<e):
        print('{}的算数平方根为{:.4f}'.format(x,g))
        break
    g = (g+x/g)/2
    
