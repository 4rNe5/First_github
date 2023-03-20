b = 0
a = 0
c = 0
while a >= 0:
  a = float(input("숫자를 입력하세요  : "))
  if a == 0:
    break
  b = b + a
  c = c + 1
  if c == 1:
    c = c + 1

print(b/(c-1))


