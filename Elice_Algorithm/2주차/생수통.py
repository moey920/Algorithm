bucket = [int(input()) for i in range(3)] # range(n)줄의 입력을 받아 리스트로 저장하기! 물병값 리스트 받기
cap = [int(input()) for i in range(2)] #뚜껑값 리스트 받기

bucket.sort() # 오름차순으로 물병 리스트 정렬하기, 리스트.sort(reverse=True) : 내림차순 정렬
cap.sort()

print(bucket[0] + cap[0] + 10)
