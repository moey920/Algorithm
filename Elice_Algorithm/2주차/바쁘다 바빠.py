N = [int(input()) for i in range(4)]
count = 0

for i in range(len(N)) :
    count += N[i]
    
print(count//60)
print(count%60)
