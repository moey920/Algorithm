# 자료구조와 알고리즘

- 프로그램의 기본 구성

> Input -> Process(<->Stroe) -> Output

- 프로그래머의 사고방식 1

> 데이터의 흐름과 저장 - 자료구조(프로그램 기본 구성의 화살표)
> 시간과 공간의 효율성 - 알고리즘(프로세스)

## 자료구조

- 자료구조 종류
    - 정수
    - 실수
    - 문자
    - 배열
    - 해쉬
    - 링크드리스트
    - 스택
    - 큐
    - 트리
    - 그래프

- 때와 장소에 맞는 자료구조(Optimized)가 필요하다.

## 알고리즘

- 좋은 알고리즘의 조건
    - 적절한 입력
    - 적절한 출력
    - 명확성(코드가 어떤 수행을 위해 존재하는가)
    - 유한성(무한루프에 빠지면 안된다)
    - 효율성

자료구조 -> 알고리즘 : 자료구조를 활용하여 어떤 문제를 해결한다.
알고리즘 -> 자료구조 : 알고리즘을 이용하여 자료구조를 구현한다.

![image.png](./image.png)

### 두 수의 합

숫자들의 배열이 주어지고 표적 숫자가 주어졌다고 합시다.배열에 주어진 숫자들 중 두 개의 숫자를 더하면 표적 숫자가 되는데요, 이때 어떤 두 수를 더하면 표적숫자가 되는지 찾는 문제를 풀어 봅시다.예를 들어서, [2, 8, 19, 37, 4, 5] 가 배열로 주어지고 12 가 표적으로 주어지면 8,4 를 찾아내시면 됩니다.

- 입력 배열에는 중복되는 수가 없습니다.
- 입력 배열에는 합해서 표적이 되는 어떤 두 수가 반드시 있습니다.
- 출력의 순서는 상관 없습니다. 위 예시의 경우, 8,4 와 4,8은 둘 다 정답으로 인정합니다.

```
def twoSum(nums, target):
    # 시간초과 나는 방법
    # for i in nums :
    #     if (target - i) in nums : 
    #         return i, target - i
    
    nums.sort()
    i = 0
    j = len(nums) - 1
    
    while i < j :
        sum = nums[i] + nums[j]
        if sum == target :
            return nums[i], nums[j]
        elif sum > target :
            j -= 1
        else :
            i += 1

def main():
    print(twoSum([2, 8, 19, 37, 4, 5], 12)) # (4, 8) 혹은 (8, 4)가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
```

### 가장 큰 두 수의 차

0보다 큰 정수들의 배열이 주어졌다고 합시다. 여기서 가능한 모든 서로 다른 두 숫자의 차이를 고려 해 보고, 이중 가장 큰 차이를 반환하는 함수를 적어봅시다. 예를 들어서, [2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23] 가 입력으로 주어졌을 경우 가장 큰 차이를 내는 숫자쌍은 50-1 = 49 입니다.

- 두 수의 차에 해당하는 값을 반환하면 됩니다. 위 예시의 경우, 49를 반환합니다.
- 양의 값을 반환해야 합니다. 위 예시의 경우 -49가 아니라 49를 반환해야 합니다.
- 배열의 길이는 2보다 크거나 같다고 가정합니다.

```
def maxTwoDiff(nums):
    return max(nums) - min(nums) # O(N)
    
    # nums.sort() # O(NlogN)
    # return nums[-1] - nums[0]
    # # nums[-1] = nums[len(nums) - 1]

def main():
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # 49가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
```

### 배열의 회전

배열을 회전 시켜봅시다. 정수들이 포함되어 있는 배열과, 숫자 k가 입력으로 주어집니다. 이때 해당 배열을 k 만큼 회전 시켜 봅시다.

예를 들어서, [1, 2, 3, 4, 5, 6, 7, 8, 9] 와 4가 입력으로 주어졌을 경우 [6,7,8,9,1,2,3,4,5] 를 반환하면 됩니다.

- k 는 배열의 길이 n 보다 작다고 가정합시다.
- 다양한 방법으로 풀어 보도록 합시다.
- (추가) 공간 복잡도 O(1)으로 풀 수 있는 방법도 생각 해 봅시다. 이때 주어진 함수 partialReverse를 활용해도 됩니다.
- 회전 방향이 주어지지 않았으니 직접 오른쪽 회전인지 왼쪽 회전인지 input을 달리하여 확인해봐야합니다.
```
# 이 함수를 수정 해 주세요.
def rotateArray(nums, k):
    # return nums[k+1:] + nums[:k+1]
    return nums[-k:] + nums[:-k]
    # nums[-1] = 9, nums[-2] = 8, nums[-1:-3] = [], nums[-3:-1] = 7, 8, nums[1:3] = 2, 3, nums[3:1] = []
    # 인덱스 순서에 맞추어 슬라이싱해야 값을 뽑을 수 있다. 
    # nums[-1:-3:-1] = [9, 8] 거꾸로 읽는 것도 가능하다.
    
    
# 다음 함수는 추가적인 공간 사용 없이 배열의 일부를 뒤집어 주는 함수입니다.
# 예를 들어, nums = [1,2,3,4,5]
# partialReverse(nums, 1, 3)
# 을 실행 할 경우, nums = [1, 4, 3, 2, 5] 가 됩니다.
# 필요하다면 사용하세요.
def partialReverse(nums, start, end):
    for i in range(0, int((end-start)/2) + 1):
        temp = nums[start + i]
        nums[start+i] = nums[end - i]
        nums[end -i] = temp


def main():
    nums = [1,2,3,4,5]
    partialReverse(nums, 1, 3) # [1, 4, 3, 2, 5] 를 반환합니다.
    print(nums)
    print(rotateArray([1,2,3,4,5,6,7,8,9], 4)) # [6,7,8,9,1,2,3,4,5] 를 반환해야 합니다.
    

if __name__ == "__main__":
    main()
```

### 아나그램 탐지

아나그램(Anagram)은 한 문자열의 문자를 재배열해서 다른 뜻을 가지는 다른 단어로 바꾸는 것을 의미합니다.

두 개의 문자열이 주어졌을 때, 서로가 서로의 아나그램인지 아닌지의 여부를 탐지하는 함수를 만들어 보세요.

- elice 와 leice 는 아나그램입니다. True를 리턴해야 합니다.
- cat 과 cap 는 아나그램이 아닙니다. False 를 리턴해야 합니다.
- iamlordvoldemort 와 tommarvoloriddle 은 아나그램입니다. True를 리턴해야 합니다.
- 문자열의 모든 문자는 영어 소문자라고 가정합시다.
```
def isAnagram(str1, str2):
    # sort활용, 시간복잡도가 NlogN이라 불편쓰
    # if sorted(str1) == sorted(str2) : # O(NlonN)
    #     return True
    # else :
    #     return False
    
    # 2번 풀이 dict 2개 활용
#     dict1 = {} # dict()
#     dict2 = {} 
    
#     for i in str1 :
#         if i not in dict1 :
#             dict1[i] = 1
#         else :
#             dict1[i] += 1
#     for i in str2 :
#         if i not in dict2 :
#             dict2[i] = 1
#         else :
#             dict2[i] += 1
#     print(dict1, dict2)
#     if dict1 == dict2 :
#         return True
#     else :
#         return False

    # 1번 풀이 dict 1개 활용
    # O(N)
    counter = {}

    for i in str1:
        counter[i] = counter.get(i, 0) + 1

    for i in str2:
        counter[i] = counter.get(i, 0) - 1

    return all(n == 0 for n in counter.values())
    
def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
    print(isAnagram('cat', 'cap')) #should return False
    

if __name__ == "__main__":
    main()
```

# 객체

> 객체 : 상태(속성, State, property) + 행동(Behavier, Method)

- 자동차 객체
    - 상태 : 색상, 모델 연도 등
    - 행동 : 가속, 정지 등

## 프로그래밍 언어의 종류

1. 절차지향 프로그래밍(C 등) <-> 객체지향 프로그래밍(Java, Python, C++, C# 등)

### 객체지향 프로그래밍의 특징

1. 캡슐화 : 코드를 묶어서 정리, 정보 은닉
2. 상속 : 기존 코드의 재활용
3. 다형성 : 코드를 더 간단하게

### 객체 예제

자동차 객체
Python은 세상의 모든 것을 객체(object)로 바라봅니다.

이 문제에는 자동차 객체가 주어져 있는데요, 아직 불완전한 상태입니다.

객체에 변수와 함수들을 추가해서 완성 해 봅시다.

- 변수 color를 추가 해 봅시다.
- 함수 speedDown을 추가 해 봅시다.
- 함수 changeColor를 추가 해 봅시다.
- 함수 wheelChange의 내용을 변경 해 봅시다.

```

class Car:
    def __init__(self):
        self.speed = 0
        self.year = 2017
        self.wheel = Wheel("aluminum") # Wheel 이라는 클래스
        # 1. 여기에 새로운 오브젝트 변수, color를 추가 해 주세요.
        # 색은 기본적으로 "white"로 설정되도록 해 주세요
        self.color = "white"
        
    def speedUp(self, addSpeed):
        self.speed += addSpeed
        
    # 2. 여기에 새로운 오브젝트 함수, speedDown을 추가해 주세요
    # 변화시키고 싶은 속도량을 입력 받은 후, 그만큼 속도록 감소시키는 일을 하는 함수입니다.
    def speedDown(self, subSpeed) :
        self.speed -= subSpeed
    
    # 3. 여기에 새로운 함수, changeColor를 추가 해 봅시다.
    # 변화시키고 싶은 색을 지정하면, 그 색깔로 차를 도색하는 함수입니다.    
    def changeColor(self, color):
        self.color = color

    def wheelChange(self, newWheelType):
        self.wheel.wheelType = newWheelType
        # 4. 객체의 데이터로 다른 객체를 사용 할 수도 있습니다. 
        # Car 객체는 Wheel 객체를 변수로 가지는데요, 
        # 여기에는 새 바퀴의 색상을 입력받고(newWheelType), 이를 바탕으로 새로운 Wheel 객체를 만들어서
        # 자동차의 wheel 데이터에 할당 하는 함수를 적어 봅시다.
    

class Wheel:
    def __init__(self, newWheelType):
        self.wheelType = newWheelType

def main():
    audi = Car()
    print("고객님의 차량은 {} 년에 출고되었습니다.".format(audi.year))
    print("현재 속도는 {} km/h 입니다.".format(audi.speed))
    audi.speedUp(200)
    print("변경된 속도는 {} km/h 입니다.".format(audi.speed))
    audi.speedDown(50)
    print("변경된 속도는 {} km/h 입니다.".format(audi.speed))
    
    print("현재 차량 색깔은", audi.color, "입니다.")
    audi.changeColor('black')
    print("변경된 차량색깔 :", audi.color)
    
    randomWheel = Wheel("aluminum")
    print("바닥에 {} 재질의 바퀴가 떨어져 있습니다.".format(randomWheel.wheelType))
    audi.wheelChange('plastic')
    print("변경된 휠 타입 :", audi.wheel.wheelType)
    
if __name__ == "__main__":
    main()
```

### 가장 큰 부분합 구하기(카데인 알고리즘[DP])

가장 큰 부분합 구하기
정수들의 리스트가 입력으로 들어옵니다. 이 정수들의 리스트를 일부분만 잘라내어 모두 더했을 때의 값을 부분합이라 부릅니다. 이때 가장 큰 부분합을 구해봅시다.

예를 들어, [-10, -7, 5, -7, 10, 5, -2, 17, -25, 1]이 입력으로 들어왔다면 [10, 5, -2, 17]을 모두 더한 30이 정답이 됩니다.

- 입력에는 최소 하나 이상의 양수가 존재합니다.
- 이 문제에는 여러 종류의 풀이법이 존재합니다. 각 풀이법의 시간 복잡도를 고려하면서 여러가지 방법으로 문제를 풀어 봅시다.
- Brute Force 방식은 O(N^2), DP 방식은 O(N)의 시간 복잡도를 갖는다.

```
# https://juneyr.dev/2019-11-21/maximum-subarray 참고하기
# 카데인 알고리즘 활용 - DP
# 각각의 인덱스 값은 이전 인덱스가 갖고 있는 최대 부분합을 연장할지, 아니면 자신의 값으로 초기화할지 그저 선택을 하면된다.
def maxSubArray(nums):
    best = 0
    end = 0
    
    for num in nums :
        end = max(num, end+num)
        # print(end)
        best = max(end, best)
        # print(best)
        
    return best
    
def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1])) # 30이 리턴되어야 합니다

if __name__ == "__main__":
    main()
```
