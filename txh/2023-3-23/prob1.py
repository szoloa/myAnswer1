for i in range(1,101):
    for j in range(2,i+1):
        if i == j:
            print(i,end=' ')
        if i%j==0:
            break
