a = [[None]*5 for i in range(5)]
k = 1
x = 4
for ai in range(5):
  x = 4
  for ab in range(5):
    if(ai == 0, ai == 2, ai == 4):
      a[ai][ab] = k
      k = k + 1
    if (ai % 2 == 1):
      a[ai][ab+x] = k
      x = x - 1
      k = k + 1

for ai in range(5):
  print(a[ai][0], a[ai][1], a[ai][2], a[ai][3], a[ai][4])
