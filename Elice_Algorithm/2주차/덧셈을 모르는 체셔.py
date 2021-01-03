N = list(input())
count = 0


for i in range(len(N)) :
    if int(N[i]) == 0 : #N[i]가 0이여서 10의 자리로 바뀐다면
        count += int(N[i-1])*10 #10의 자리 숫자인 N[i-1]에 10을 곱하여 count변수에 더해주고
        count -= int(N[i-1]) # N[i-1]이 일의 자리로 생각된 상태에서 이전에 더해진 count 변수를 빼주고 
    count += int(N[i]) # 그 외의 상황에는 N[i] 일의 자리 수를 더해준다.
print(count)
