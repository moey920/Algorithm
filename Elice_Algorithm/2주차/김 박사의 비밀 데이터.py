N = int(input())
code = [int(input()) for i in range(N)]
check_code = 0

for i in range(len(code)) :
    check_code += code[i]
    
check_code = str(check_code)

print(check_code[0:10])
