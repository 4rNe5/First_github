a = [None]*10
b = 0

while b <= 9:
  a[b] = int(input())
  b = b + 1

fst = 0
scd = 1

while fst <= 9:
  if a[fst] > a[scd]:
    a[fst],a[scd] = a[scd],a[fst]
    scd = scd + 1
fst = fst + 1
scd = fst + 1

