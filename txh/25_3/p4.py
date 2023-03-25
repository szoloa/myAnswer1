ph = int(input())

if ph == 7 :
    print('ph值等于7，溶液为中性')
elif ph <7 & ph>=0:
    print('ph值在[0,7)区间内，溶液为酸性')
elif ph <=14 & ph >=8:
    print('ph值在[8,14]区间内，溶液为碱性')