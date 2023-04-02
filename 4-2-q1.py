a = [None]*10
for n in range(0,10,1):
  a[n] = int(input())

wcnt = [1]*10

for cnt in range(0,10,1):
  for kk in range(0, 10, 1):
    if a[cnt] < a[kk]:
      wcnt[cnt] = wcnt[cnt] + 1


for cnt in range(0,10,1):
  print(a[cnt],wcnt[cnt],"등")

'''
while cnt <= 10:
  if a[cnt] > a[cnt1]:
    wcnt[cnt] = w
    wcnt[cnt1] = w+1
  if a[cnt] < a[cnt1]:
    wcnt[cnt1] = w
    wcnt[cnt] = w+1
  if a[cnt] == a[cnt1]:
    wcnt[cnt] = w
    wcnt[cnt] = w
  cnt += 1

  wcnt += 1
  w += 1
'''
