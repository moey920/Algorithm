N = [int(input()) for i in range(10)]

for i in range(len(N)) :
    N[i] = N[i] % 42

N = set(N)
print(len(N))
'''
set 함수 이용하기. set : 중복을 허용하지 않는 자료형태
list를 set으로 형변환 했다가, 다시 list로 형변환하면 중복이 제거된 list를 얻을 수 있다.
'''