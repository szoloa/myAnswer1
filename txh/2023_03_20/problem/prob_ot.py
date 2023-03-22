num = num_r = int(input())
rate = float(input())
min = 0
while num <= num_r*2 :
    num = num*(1+rate)
    min += 1
print(min)