#백준1202번_보석도둑 (2022.01.23)

import sys

n,k = map(int,sys.stdin.readline().split())
bosuk = []
bag = []
cost = 0

for i in range(n):
  bosuk.append(list(map(int,sys.stdin.readline().split())))

for i in range(k):
  c = int(sys.stdin.readline())
  bag.append(c)

bag.sort()
bosuk.sort(reverse=True,key=lambda x:(x[1]))

print(bag)
print(bosuk)

for i in bag:
  for j in bosuk:
    if i >= j[0]:
      cost += j[1]
      bosuk.remove(j)
      break

print(cost)

      