a = [None]*10
b = 0

while b <= 9:
  a[b] = int(input("숫자 입력 : "))
  b = b + 1

b = 0
oputt = 0
while b <= 9:
  if a[b] > 50:
    oputt = oputt + a[b]
  b = b + 1

print(oputt)
