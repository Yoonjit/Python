# 선택 정렬 알고리즘

def selection_sort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i, len(a)): # 정렬 안 된 부분에서 최솟값 찾기
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i] # 현재 원소와 최솟값 가진 원소 교환

a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]

print()
print('# 선택 정렬 알고리즘')
print('정렬 전: ', end='')
print(a)

selection_sort(a)

print('정렬 후: ', end='')
print(a)
print()


# 삽입 정렬 알고리즘

def insertion_sort(b):
    for i in range(1, len(b)): # 현재 원소의 인덱스
        for j in range(i, 0, -1): # 현재 원소가 정렬된 부분에 삽입될 곳을 찾음
            if b[j-1] > b[j]: 
                b[j], b[j-1] = b[j-1], b[j] # 현재 원소와 직전 원소 교환

b = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]

print('# 삽입 정렬 알고리즘')
print('정렬 전: ', end='')
print(b)

insertion_sort(b)

print('정렬 후: ', end='')
print(b)
print()


# 버블 정렬 알고리즘

def bubble_sort(c):
    n = len(c)

    for i in range(n-1, 0, -1):
        bChanged = False

        for j in range(i):
            if(c[j] > c[j+1]):
                c[j], c[j+1] = c[j+1], c[j]
                bChanged = True

        if not bChanged:
            break
        print(c, n-i)


# 쉘 정렬 알고리즘

def shell_sort(d):
    n = len(d)
    gap = n // 2 # 최초 gap: 리스트 크기의 절반

    while gap > 0:
        if(gap % 2) == 0: # 짝수
            gap += 1 

        for i in range(gap):
            sortGapInsertion(d, i, n-1, gap)

        print('    Gap = ', gap, d)
        gap = gap // 2 # gap을 절반으로 줄임

def sortGapInsertion(d, first, last, gap):
    for i in range(first+gap, last+1, gap):
        key = d[i]
        j = i + gap

        while j >= first and key < d[j]: # 삽입 위치 찾기
            d[j+gap] > d[j] # 항목 이동
            j -= gap

        d[j+gap] = key

    
# 리스트에서 4와 7을 제거하기

list = [1, 3, 4, 4, 3, 2, 7, 4, 1, 7, 4]
del_list = [4, 7]

print('원래 list: ',  end='')
print(list)

for x in del_list:
    while x in list:
        list.remove(x)

print('4와 7을 제거한 뒤의 list: ', end='')
print(list)
print()


# 최상위 3개를 제거하고 리스트 출력(원래 순서 유지)

list = [-3.2, 5.5, 4.1, 1.1, -1.3, 2.7, 0.5]

temp = list.copy()
temp.sort(reverse = True) # 내림차순 정렬

print(f'내림차순 정렬 list: {temp}')

for x in temp[:3]:
    while x in list:
        list.remove(x)

print(f'최상위 3개를 제거한 후의 list: {list}')

print()