# 동적계획법

1. 피보나치 수열
```
def fibo(n) :
    if n < 3 :
        return 1
    else :
        dp[n] = dp[n-1] + dp[n-2]
```
- 한번 계산 했던 것을 또 계산한다. dp[5]를 얻기 위해선 dp[4]와 dp[3]이 필요한데 dp[4]를 얻기위해선 dp[3]과 dp[2]기 필요하기 때문에 dp[3]을 두 번 구해야한다.
    - 항상 알고리즘 문제를 풀다보면 이러한 재귀를 잘 쓰지 못해서 메모리가 과다하게 사용되는 경우가 많았다. 

2. 재귀를 이용한 피보나치 수열
3. 동적계획법 : 복잡한 문제를 간단한 여러 개의 하위 문제로 나누어 푸는 방법 (Cache와 Memoization!)
> 하위 문제의 답을 **저장**해서 중복 연산을 하지 않는다!!!
```
fibonacci = {1:1, 2:1} # Cache
def fibo(n) :
    if n in fibonacci : # 이미 구하고자 하는 n번째 값이 저장이 되어 있다면!!(하위문제의 답)
        return fibonacci[n] # 값을 구하지 않고 바로 리턴한다 -> Memoizition
    else : 
        fibonacci[n] = fibo(n-1) + fibo[n-2] # 구하고자하는 n번째 값이 dictionary에 없다면 답을 구해서
        return fibonacci[n] # 값을 저장한다
```
- 특징
    - 중복되는 부분문제(overlapping subproblems)
    - 최적 부분 구조(optimal substructure) : 최적해는 부분 문제의 최적해로부터 구할 수 있다.

- 분할정복법과 동적계획법의 차이
    - 분할정복을 통해 31524를 정렬하기.
        - 31 / 524
        - 3 / 1 / 5 / 2 / 4
        - 13 / 245
        - 12345
    - 동적계획법의 중복되는 부분문제라는 점이 동일하다. 

4. 시간/공간 복잡도 계산
- 단순한 재귀호출과 동적계획법 사용이 시간 복잡도에서 어떤 차이를 보일까?
    - 재귀호출 : 기저조건에 다다르면 조건이 달라지지만, 보통 지수적으로 계산이 반복된다. 현실적으로 쓰기 어려움. 계산량이 너무 많다.
    - 동적계획법 : 한번 계산 해놓은 값을 계산하지 않기 때문에 N번만 계산한다. 계산을 위한 재귀를 돌지 않는다. = O(N)
- 공간 복잡도 :
    - 동적계획법 : 하위 문제의 답을 모두 저장하기 때문에 하위문제의 수만큼 저장공간이 필요하다.

5. 동적 계획법을 구현하는 테크닉
> 점화식 : 복잡한 문제를 작은 하위문제로 표현한 시

    - 구하고자 하는 값이 무엇인지 정의한다
        - f(n) : n번째 피보나치 수열
    - 구하고자 하는 값을 부분문제로 표현한다.
        - f(n) = f(n-1) + f(n-2)

    - Top-down(재귀호출 식)
        - 큰 문제를 작은 문제로 나누어 풀기
        - 작은문제를 풀어 return 해준다.
```
fibonacci = {1: 1, 2: 1}
def fibo(n):
    if n in fibonacci:
        return fibonacci[n]
    else:
        fibonacci[n] = fibo(n-1) + fibo(n-2)
        return fibonacci[n] 
```

    - Bottom-up(반복문)
        - 작은 문제부터 차례로 풀어 적는다
        - 크기를 조금씩 늘려서 문제를 푼다
        
```
def fibo(n):
    fibonacci = [-1, 1, 1]
    if n < 3: return 1
    for i in range(3, n+1):
        fibonacci.append(
        fibonacci[i-1] + fibonacci[i-2])
    return fibonacci[n]
```
