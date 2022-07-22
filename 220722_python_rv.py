# 2) upper(), lower()
# 해당 함수들을 사용할 때 원본이 바뀌는 건 아님 = 비파괴적 함수
# 원본을 아예 새로운 것으로 바꿔버리는 파괴적 함수도 있음 ex. append()

lyrics = "Everybody but your dog, you can all FUCK OFF"
print(lyrics.upper()) # 대문자로 변환
print(lyrics.lower()) # 소문자로 변환

print()


# 3) strip(): 문자열 양 옆의 공백을 제거 (lstrip, rstrip)
# 여기서 공백의 의미: 띄어쓰기, 탭, 줄 바꿈
# trim(다듬기) 함수의 일종

a = "   오늘 저녁 뭐 먹지   "
print(a)
print(a.strip())

b = """
아메리카노 좋아 좋아 좋아
아메리카노 진해 진해 진해
"""
print(b, "\n-------------------------")
print(b.lstrip(), "\n-------------------------")
print(b.rstrip(), "\n-------------------------")
print(b.strip(), "\n-------------------------")

print()


# 4) is~~~(): 논리값이 반환됨

print('1', "123abc456DEF".isalnum()) # alpha + number, 알파벳이나 숫자로만 구성되어 있는가?
print('2', "abcdef12".isalpha()) # 알파벳으로만 구성되어 있는가?
print('3', "        ".isspace()) # 공백으로만 구성되어 있는가?
print('4', "ABCDEF".isupper()) # 대문자로만 구성되어 있는가?
print('5', "abcedF".islower()) # 소문자로만 구성되어 있는가?
print('6', "123abc".isidentifier()) # 이 문자열을 이름으로 하는 변수나 함수를 만들 수 있는가? (식별자로 사용이 가능한지)

a = '12345678'
print('isdigit', a.isdigit()) # 셋 다 숫자인지 판별하는 함수인데 약간씩 차이가 있음
print('isdecimal', a.isdecimal())
print('isnumeric', a.isnumeric())

b = '3²'
print('isdigit', b.isdigit()) # '숫자처럼 생긴 모든 글자'를 숫자로 판별하여 T 반환
print('isdecimal', b.isdecimal()) # 특수문자 인정 안 함, 정수 형태인지를 판별하므로 F 반환
print('isnumeric', b.isnumeric()) # 제곱근, 분수, 거듭제곱, 특수문자 인정 = 숫자값 표현 인정, T 반환

print()


# 5) find(): 왼쪽부터 탐색해 특정 문자가 처음 등장하는 index를 찾음
# rfind()는 오른쪽부터 탐색함

print("안녕안녕안녕하세요".find("안녕")) # 0
print("안녕안녕안녕하세요".rfind("안녕")) # 4

print()


# 6) in: 논리값이 반환됨

print("안녕" in "안녕하세요")
print("안냥" in "안녕하세요")

print()


# 7) split(): 특정 문자를 기준으로 문자열을 잘라서 리스트로 만듦

str = """
내 앞에 있는 안내 근무자의 안내를 받아
한 자리에 두 분씩 한 보트에 열 분이서
머리 젖습니다 옷도 젖습니다
신발 젖습니다 양말까지 젖습니다
옷 머리 신발 양말 다 다 젖습니다
"""
print(str.strip().split())