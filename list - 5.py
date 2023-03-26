a = [None]*10
b = 0

while b <= 9:
  a[b] = int(input())
  b = b + 1

b = 0
bigwin = 0
smlwin = 0
meet = 0

while b <= 9:
  if bigwin < a[b]:
    bigwin = a[b]
  b = b + 1

b = 0
smlwin = bigwin
while b <= 9:
  if smlwin > a[b]:
    smlwin = a[b]
  b = b + 1

b = 0
while b <= 9:
 meet = meet + a[b]
 b = b + 1

x = bigwin + smlwin
oput = (meet - x) / 8
print(oput)

