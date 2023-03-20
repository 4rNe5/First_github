a=int(input("학번을 입력하세요 : "))
b=int(input("시험 점수를 입력하세요 : "))

if b>=90:
    print(a,"님은 \"조기졸업\"")
elif b>=60:
    print(a,"님은 \"정상졸업\"")
elif b<60:
    print(a,"님은 \"여름 방학 재수강\"")
else:
    print(a,"님은 \"졸업불가\"")
