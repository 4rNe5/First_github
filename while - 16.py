endcnt = 0
fcnt = 0
scnt = 0
tcnt = 0
focnt = 0
allman = 0

while endcnt == 0:
  snum = int(input("학번을 입력하세요 : "))
  tsco = float(input("시헙점수를 입력하세요 : "))
  if tsco == -1:
    break #while 탈출
  if tsco >= 90:
    print(snum, "님은 \"조기졸업\"")
    fcnt = fcnt + 1
  elif tsco >= 60 or tsco < 90:
    print(snum, "님은 \"정상졸업\"")
    scnt = scnt + 1
  elif tsco >= 1 or tsco < 60:
    print(snum, "님은 \"여름 방학 재수강\"")
    tcnt = tcnt + 1
  elif tsco == 0:
    print(snum, "님은 \"졸업불가\"")
    focnt = focnt + 1

#탈출 후 실행
allman = fcnt + scnt + tcnt + focnt #전체 인원 수 계산

print("입력하신 인원수는 모두",allman,"명입니다")
print("조기졸업 인원은",fcnt,"명입니다")
print("정상졸업 인원은",scnt,"명입니다")
print("여름방학 재수강 인원은",tcnt,"명입니다")
print("졸업불가 인원은",focnt,"명입니다")




