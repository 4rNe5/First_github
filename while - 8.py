b = 3
c = int(input("숫자를 입력하세요 : "))
d = c
while b >= 1:
  while c >= 1:
    print("*", end="")
    c = c - 1
  print("")
  c = d
  b = b - 1
