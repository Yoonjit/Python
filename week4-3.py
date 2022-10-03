# 마라톤

num = int(input('마라톤 선수의 총 인원수를 입력하세요: '))
list = []
dict = {}

for i in range(num):
    id = int(input('마라톤 선수의 참가번호를 입력하세요: '))
    list.append(id)

for i in list:
    rec = int(input('마라톤 선수의 기록을 입력하세요(초 단위): '))
    dict[i] = rec

lank = sorted(dict.items(), key = lambda x: x[1])

for i in range(3):
    hour = (lank[i][1] // 3600)
    min = (lank[i][1] % 3600) // 60
    sec = (lank[i][1] % 3600) % 60
    print('%d위 (번호, 시, 분, 초) >>' % (i+1), lank[i][0], hour, min, sec)