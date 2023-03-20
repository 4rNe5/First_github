a = 0
b = int(input("원하는 숫자를 입력하세요 : "))
c = 0

while b > 0:
  if b % 2 == 1:
    c = c + b
  b = b - 1

print("정답 : ",c)
