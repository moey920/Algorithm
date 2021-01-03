a = map(int, input().split())
b = map(int, input().split())

sum1 = sum(list(a))
sum2 = sum(list(b))

if sum1>=sum2 :
    print(sum1)
else :
    print(sum2)
