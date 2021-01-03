N = [int(input()) for i in range(3)]
multi = N[0]*N[1]*N[2]
multi = str(multi)

for i in range(10) :
    int_i = multi.count(str(i))
    print(int_i)


# 포함(Containment) 연산자(in, not in)?
# 문자열 객체의 count() 메서드는 문자열에서 특정 문자의 개수를 리턴한다.