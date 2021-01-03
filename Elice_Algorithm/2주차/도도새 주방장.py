dodo = list(map(int,input().split()))
cook_time = list(map(int,input().split()))
sum_cook = 0
count = 0

        
for i in range(len(cook_time)) :
    if(sum_cook + cook_time[i] > dodo[1]) :
        break
    else :
        count += 1
        sum_cook += cook_time[i]

print(count)
