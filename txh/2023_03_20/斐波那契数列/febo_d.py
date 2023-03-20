def feb(n):
    if n == 1 or n == 2:
        return 1
    return feb(n-1) + feb(n-2)
n = int(input())
for i in range(1,n+1):
    print(feb(i))