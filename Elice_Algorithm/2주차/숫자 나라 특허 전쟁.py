N = int(input())
count = 0

for i in range(N) :
    if i%3 == 0 :
        count += i
    elif i%5 == 0 :
        count += i
        
print(count)
