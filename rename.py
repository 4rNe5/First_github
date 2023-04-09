# Created on 4 / 9, Sunday
# Created by 4rNe5

a = [None]*10
aa = [1]*10

for x in range(0,10,1):
  a[x] = int(input())

for c in range(0,10,1):
  for k in range(0,10,1):
    if a[c] < a[k]:
      aa[c] = aa[c] + 1

for c in range(0,10,1):
  print(a[c], aa[c], "등입니다.")

