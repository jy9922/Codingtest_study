import sys

n = list(sys.stdin.readline())
count = 0
a = []

for i in n:
  if i.isnumeric():
    count = count + int(i)
  else:
    continue
    
n.sort()

for i in n:
  if i.isnumeric():
    continue
  else:
    a.append(i)
    
a.append(str(count))

print(''.join(a))