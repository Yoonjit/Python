# git reset --hard 헤드 주소
# git push -f origin master

a = 10
a **= 2
print('a는', a) # 문자열과 변수 사이에 자동으로 공백 생김

str = '우영우'
str += '영우' # 문자열에서의 복합 대입 연산자는 +, *만 가능 (-= X)
print(str)

for i in range(4):
    str += '영우'
print(str)
print()

i1 = input('논리값 입력: ')
i2 = input('숫자 입력: ')
print(type(i1)) # input으로 입력받은 것은 자료형이 무조건 문자열 형식
print(type(i2))
print()

# <cast: 자료형 변환>
num1 = int(input('숫자 입력: '))
num2 = int(input('숫자 입력: '))
print(num1 + num2)

# <swap>
a = 12
b = 34
print(a, b)
c = a
a = b
b = c
print(a, b)

# <에러의 종류>
# 3) ValueError: 변환할 수 없는 것을 변환하려고 할 때 발생
#    ex. int("123.45") -> 실수 형태의 문자열을 정수로 바꾸려고 함