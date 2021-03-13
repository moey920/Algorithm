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
4. 시간/공간 복잡도 계산
