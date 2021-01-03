# 100점을 맞긴 했는데, 도저히 깔끔하다고 생각이 안됨. 다시 생각해보기..

N = int(input())
B = list(map(int, input().split()))
a = []
b = []
count = 0

for i in range(N) :
    count = B[i]*(i+1)
    a.append(count)
    b.append(count-a[i-1])

b[0] = a[0]

for i in range(N) :
    print(b[i], end=' ')
