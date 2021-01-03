N,K = map(int, input().split())
count = 0

for n in range(N+1) :
    count += n**K 

mod = count % 1000000009
print(mod)
