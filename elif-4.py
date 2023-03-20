a=int(input("첫 번째 사람의 태어난 달 : "))
b=int(input("두 번째 사람의 태어난 달 : "))
if a==3 or a==4 or a==5:
  c = 1
if a==6 or a==7 or a==8:
  c = 2
if a==9 or a==10 or a==11:
  c = 3
if a==12 or a==1 or a==2:
  c = 4

if b==3 or b==4 or b==5:
  d = 1
if b==6 or b==7 or b==8:
  d = 2
if b==9 or b==10 or b==11:
  d = 3
if b==12 or b==1 or b==2:
  d = 4

if c == d:
  print("두 사람의 태어난 계절이 같습니다.")
else:
  print("두 사람의 태어난 계절이 다릅니다.")
