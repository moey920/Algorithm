N = int(input())
score = list(map(int, input().split()))
high = max(score)

for i in range(len(score)) :
    score[i] = (score[i]/high)*100

print(sum(score)/len(score))