a = [None]*10
b = 0

while b <= 9:
  a[b] = int(input())
  b = b + 1

b = 0
bigwin = 0

while b <= 9:
  if bigwin < a[b]:
    bigwin = a[b]
  b = b + 1
print("가장 큰 수는",bigwin,"입니다.")
