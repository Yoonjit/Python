# 마라톤 문제 정렬 알고리즘으로 풀기

# 입력받는 것: 총 인원수, 선수 각각의 참가번호, 선수 각각의 기록

def selection_sort(a): # 선택 정렬 알고리즘
    for i in range(0, len(a)-1):
        min = i
        for j in range(i, len(a)): # 정렬 안 된 부분에서 최솟값 찾기
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i] # 현재 원소와 최솟값 가진 원소 교환

num = int(input('마라톤 선수의 총 인원수를 입력하세요: '))
lis = []
dic = {}

for i in range(num):
    id = int(input('마라톤 선수의 참가번호를 입력하세요: ')) # key
    lis.append(id)

for i in lis:
    rec = int(input('마라톤 선수의 기록을 입력하세요(초 단위): ')) # value
    dic[i] = rec

a = list(dic.values()) # 기록으로 리스트 만들기

selection_sort(a) # 기록을 기준으로 정렬

b = [0, 0, 0]

for key, value in dic.items():
    if value == a[0]:
        b[0] = key
    elif value == a[1]:
        b[1] = key
    elif value == a[2]:
        b[2] = key

for i in range(3):
    hour = (a[i] // 3600)
    min = (a[i] % 3600) // 60
    sec = (a[i] % 3600) % 60
    print('%d위 (번호, 시, 분, 초) >>' % (i+1), b[i], hour, min, sec)