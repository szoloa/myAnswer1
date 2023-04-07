n = int(input())
m = int(input())

child = [i for i in range(1,n+1)]
childgone = []
while child:
    tim = m%len(child)
    childgone.append(child[tim])
    del child[tim]
for i in range(n):
    print(childgone[-i-1],end=' ')