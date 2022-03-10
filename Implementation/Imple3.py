n = input().split()

width = ['a','b','c','d','e','f','g','h']

for w,h in n:
  new_width = width.index(w) + 1
  h = int(h)

x,y = new_width,h
counting = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(4):
  nx = x + 2 * dx[i]
  ny = y + 2 * dy[i]

  if nx < 1 or ny < 1 or nx > 8 or ny > 8 :
    continue

  x, y  = nx, ny

  if i < 2:
    if y + 1 < 9:
      counting += 1
    if y - 1 > 0:
      counting += 1
  elif i >= 2:
    if x + 1 < 9:
      counting += 1
    if x - 1 > 0:
      counting += 1

  x,y = new_width,h
 
print(counting)




