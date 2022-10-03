# 우주선 발사
def countDown(n):
    if n == 0:
        print("발사!")
    else:
        print(n)
        countDown(n-1)
countDown(5)
print("-----------")


# 별 모양 출력
def printStar(k):
    if k > 0:
        printStar(k-1)
        print("*" * k)
printStar(5)
print("-----------")


# 별 모양 역순 출력
def printStar(k):
    if k > 0:
        print("*" * k)
        printStar(k-1)
printStar(5)
print("-----------")


# 진법 변환 (재귀)
def change(inputs, n):
    list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    if inputs < n:
        return list[inputs]
    else:
        return change((inputs // n), n) + list[(inputs % n)]

inputs = int(input("10진수 입력: "))

print('2진수: ', end = '')
print(change(inputs, 2))
print('8진수: ', end = '')
print(change(inputs, 8))
print('16진수: ', end = '')
print(change(inputs, 16))
print("-----------")


# 진법 변환 (반복문)
def change(inputs, n):
    str = '0123456789ABCDEF'
    results = ''

    while (0 < inputs):
        results += str[(inputs % n)] 
        inputs //= n

    results = results[::-1]
    return results

inputs = int(input("10진수 입력: "))

print('2진수: ', end = ''), print(change(inputs, 2))
print('8진수: ', end = ''),print(change(inputs, 8))
print('16진수: ', end = '')
print(change(inputs, 16))