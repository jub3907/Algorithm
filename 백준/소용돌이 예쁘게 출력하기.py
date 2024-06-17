#%%
# https://www.acmicpc.net/problem/1022

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r1,c1,r2,c2 = map(int,input().split())
hurricane = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]
total = (c2-c1+1) * (r2-r1+1)
direction = 1
x = 0
y = 0
cnt = 1
l = 1

while total > 0:
    for _ in range(2):
        for _ in range(l):
            if r1 <= x <= r2 and c1 <= y <= c2:
                hurricane[x - r1][y - c1] = cnt
                total -= 1
                m = cnt
            x += dx[direction]
            y += dy[direction]
            cnt += 1
        direction = (direction-1) % 4
    l += 1

max_len = len(str(m))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(hurricane[i][j]).rjust(max_len), end=" ")
    print()

#%%
import sys
input = sys.stdin.readline

def getValue(r,c):
    n=max(abs(r), abs(c))
    last= (2*n+1)**2

    if r==n:#아래 변
        return last-(n-c)
    elif c==-n:#왼쪽 변
        return last-(2*n)-(n-r)
    elif r==-n:#윗 변
        return last-(4*n)-(n+c)
    else: #오른쪽 변
        return last-(6*n)-(n+r)

r1,c1,r2,c2 = map(int,input().split())
tonado = []

for x in range(r1,r2+1):
    for y in range(c1,c2+1):
        tonado.append(str(getValue(x,y)))
    tonado.append('\n')

digit = 0
for i in range(len(tonado)):
    if tonado[i] == '\n':
        continue
    digit = max(digit,len(tonado[i]))

for i in range(len(tonado)):
    if tonado[i] == '\n':
        continue
    tonado[i] = tonado[i].rjust(digit,' ')
    
for i in range(len(tonado)):
    if tonado[i] == '\n':
        print()
    else:
        print(tonado[i],end=' ')