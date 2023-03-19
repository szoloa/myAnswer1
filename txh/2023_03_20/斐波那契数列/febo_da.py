febn = 1
febn_ = 1
n = int(input())
for i in range(n):
    febn, febn_ = febn_+febn, febn
print(febn)