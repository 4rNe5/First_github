k = float(input("체중을 입력하세요 : "))
m = float(input("신장을 입력하세요 : "))
b = k / (m*m)

if b <= 18.5:
  print("저체중입니다.")
if b > 18.5 and b < 23:
  print("정상입니다.")
if b > 24 and b < 26:
  print("과체중입니다.")
if b > 27 and b < 33:
  print("비만입니다.")
if b > 33:
  print("고도비만입니다.")
