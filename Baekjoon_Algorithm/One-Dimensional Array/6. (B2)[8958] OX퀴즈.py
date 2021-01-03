N = int(input())
OX = []
for i in range(N) :
    OX.append(str(input()))


for i in range(len(OX)) : # 문자열 리스트 OX에서 각 문자열(OX[i]) 파싱
    score = 0 # X를 만나기 전에 누적된 점수의 합
    result = 0 # 한 문자열 안에서 score를 모두 합한 총 점수
    count = 0 # X를 만나기 전 O가 몇 번 나오는지(O의 개수와 count는 같다.)
    for j in range(len(OX[i])) : # OX[i]번째 문자열에서 j번째 인덱스를 가진 문자
        if OX[i][j] == 'O' : #문자열 OX[i]의 [j]번째 인덱스인 문자가 'O'라면
            count += 1 # X를 만나기 전까지 O가 나온 개수를 카운트한다.
            score += count # O의 개수와 더해야 하는 누적합이 같기 때문에 score에 count를 더한다.
            if j == len(OX[i])-1 : # 문자열 OX[i]가 10글자라면 인덱스는 9번까지이기 때문에[문자열 끝에 다다르면]
                result += score # result에 O가 나와 쌓인 score를 더한다.
        else : 
            result += score # X를 만나면 O가 나와 쌓인 score를 더한다.
            score = 0
            count = 0
    print(result)

# print(OX)

''' 테스트 케이스
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''