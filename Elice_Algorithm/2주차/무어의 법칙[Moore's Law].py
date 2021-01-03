N = int(input())
result = 2**N
result = str(result) #16384를 각 자리수의 값으로['1','6','3','8','4']로 바꾸기 위해 문자열로 형변환을 해주었다.
count = 0
for i in range(len(result)) :
    count += int(result[i]) #['1','6','3','8','4']를 각각 더하기 위해(1+6+3+8+4) 숫자형으로 형변환을 해주었다.

print(count)
