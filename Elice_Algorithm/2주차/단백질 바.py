customer = int(input())
protein = [10, 40, 250]

pure = divmod(customer, 250) # 고객이 원하는 함량을 순수 단백질 큐브의 단백질 함유량(250)으로 나눈 몫과 나머지를 튜플로 pure에 저장
chicken = divmod(pure[1], 40) # 튜플은 인덱스사용이 가능하다. 
nuts = divmod(chicken[1], 10)

if nuts[1] != 0 :
    print(-1)
else :
    # print(nuts[0], chicken[0], pure[0]) # 원래 정답, 문제 오류로 인해 출력 순서 변경했음!
    print(pure[0], chicken[0], nuts[0])

