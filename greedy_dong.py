n, k = map(int, input().split())

result = 0

while True:
  #N이 K로 나누어 떨어지는 수가 될 때까지 빼기

  #target이라는 새로운 변수를 설정, N을 K로 나눈 몫에 다시 K를 곱함으로써
  #만약 N이 k로 나누어 떨어지지 않는다고 가정했을 때 
  #K로 나누어 떨어지는 가장 가까운 수를 찾기 위해 설정
  target = (n//k) * k
  #result는 연산을 수행하는 횟수를 의미, 1를 빼는 작업을 몇 번 수행할 지 한 번에 수행
  result += (n-target)
  n = target
  #N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)

##############################################

# while True:
#   #N이 K로 나누어 떨어지는 수가 될 때까지 빼기

#   #target이라는 새로운 변수를 설정, N을 K로 나눈 몫에 다시 K를 곱함으로써
#   #만약 N이 k로 나누어 떨어지지 않는다고 가정했을 때 
#   #K로 나누어 떨어지는 가장 가까운 수를 찾기 위해 설정
#   target = (n//k) * k
#   print("target:"+str(target))
#   #result는 연산을 수행하는 횟수를 의미, 1를 빼는 작업을 몇 번 수행할 지 한 번에 수행
#   print("변수 n :" + str(n))
#   result += (n-target)
#   print("result:"+str(result))
#   n = target
#   print("변수 n2 :" + str(n))
#   #N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#   if n < k:
#     break
#   result += 1
#   print("result2:"+str(result))
#   n //= k

# result += (n-1)
# print(result)