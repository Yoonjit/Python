# 문자열 함수

# 1) format()

# ㄱ. 숫자를 문자열로 바꾸기
# IndexError: 매개변수 개수와 실제로 들어오는 것의 개수가 다를 때 발생

str = 20000305
print("변경 전 자료형", type(str))
str = "{}".format(str)
print("변경 후 자료형", type(str))

str1 = "{}년 {}월 {}일".format(2000, 3, 5)
str2 = """\
{}초라도 안 보이면 {}렇게 초조한데
{}초는 어떻게 기다려
이야이야이야이야\
""".format(1, 2, 3)
print(str1)
print(str2)
print()


# ㄴ. 정수를 매개변수로 받을 때

str = "{:d}".format(100) # :d - 정수를 받겠다, 그리고 자료형은 문자열 형식이 됨

str1 = "{:5d}".format(111) # 마지막 자리가 5번째 칸에 오도록 함 (1이 3, 4, 5번째에 나옴)
str2 = "{:10d}".format(111) # 앞에서부터 10칸 띄고 정수 나오기 시작함 (1이 8, 9 10번째에 나옴)
str3 = "{:05d}".format(111) # :5d가 빈 칸을 공백으로 채운다면 얘는 0으로 채움
str4 = "{:010d}".format(111) # 0으로 채우는 건 되는데 다른 숫자로 채우는 건 안 됨
str5 = "{:05d}".format(-111) # -0111
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print()


# ㄷ. 기호를 붙여서 출력하기

str1 = "{:+d}".format(123) # +123
str2 = "{:+d}".format(-123) # -123

str3 = "{:-d}".format(123) # 123, {} 안에 - 쓰는 건 의미 없음
str4 = "{:-d}".format(-123) # -123, -끼리 상쇄되고 그런 거 없음
str5 = "{: d}".format(123) # (공백)123
str6 = "{: d}".format(-123) # -123, 공백 사라짐


# ㄹ. 여러 가지 기호 조합
# 순서: (: = +- 0 숫자)
# '=' 기호가 들어가면 부호를 제일 앞에 두고 나머지가 실행됨

str1 = "{:+5d}".format(123) # (공백)+123
str2 = "{:+5d}".format(-123) # (공백)-123
str3 = "{:=+5d}".format(123) # +(공백)123
str4 = "{:=+5d}".format(-123) # -(공백)123
str5 = "{:=+010d}".format(123) # +000000123
str6 = "{:=+010d}".format(-123) # -000000123


# ㅁ. 부동 소수점

str1 = "{:f}".format(123.45) # 123.450000, 기본적으로 소수점 6번째 자리까지 출력
str2 = "{:=+15f}".format(123.45) # +(공백)(공백)(공백)(공백)123.450000

str3 = "{:10f}".format(3.141592) # (공백)(공백)3.141592
str4 = "{:10.6f}".format(3.141592) # (공백)(공백)3.141592
str5 = "{:10.5f}".format(3.141592) # (공백)(공백)(공백)3.14159
str6 = "{:10.4f}".format(3.141592) # (공백)(공백)(공백)(공백)3.1416 --> 반올림

str7 = "{:g}".format(123.0) # 123, .0과 같이 의미없는 소수점 제거 할 때 :g 사용