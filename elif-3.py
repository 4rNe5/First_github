a=int(input("국어점수 : "))
b=int(input("영어점수 : "))
c=int(input("수학점수 : "))
d=int(input("사회점수 : "))
e=int(input("과학점수 : "))

if a==0 or b==0 or c==0 or d==0 or e==0:
    print("\"졸업불가\"")
else:
    print("\"졸업가능\"")