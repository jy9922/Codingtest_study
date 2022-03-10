n = int(input())
a = list(map(int,input().split()))
result = 0

a.sort(reverse=True)

for i in a:
  m = a[0]

  if m > n:
    a.remove(a[0])
    n = n-1
  
  del a[0:m-1]
  result += 1

print(result)


