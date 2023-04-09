a = [[None]*5 for i in range(5)]
k = 1
for ai in range(5):
  for ab in range(5):
    a[ai][ab] = k
    k = k + 1


for ai in range(5):
  print(a[ai][0], a[ai][1], a[ai][2], a[ai][3], a[ai][4])
