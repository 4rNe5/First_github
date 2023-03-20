a = int(input("원하는 숫자를 입력하세요 : "))
n = 1
b = 0
c = 0
while n <= a:
  while b <= c:
    print("*",end = "")
    b = b + 1
  print("")
  b = 0
  c = c + 1
  n = n + 1
