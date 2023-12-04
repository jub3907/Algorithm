#%%
from collections import deque

def isEdge(coord, i, j):
    return coord[i][j] == 1 and (coord[i][j-1] == 0 or coord[i][j+1] == 0 or coord[i-1][j] == 0 or coord[i+1][j] == 0)

def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    corner = set()
    coord = [[0 for _ in range(100)] for _ in range(100)]
    for row in rectangle:
        sx, sy, ex, ey = row
        sx *= 2
        sy *= 2
        ex *= 2
        ey *= 2
        corner.add((sy,sx))
        corner.add((ey,ex))
        corner.add((ey,sx))
        corner.add((sy,ex))
        for i in range(sy, ey + 1):
            for j in range(sx, ex + 1):
                coord[i][j] = 1

        for another in rectangle:
            if row == another:
                continue
            else:
                asx, asy, aex, aey = another
                
                corner.add((sy,asx))
                corner.add((sy,aex))
                corner.add((ey,asx))
                corner.add((ey,aex))
                corner.add((aey,ex))
                corner.add((aey,sx))
                corner.add((asy,ex))
                corner.add((asy,sx))
                

    matrix = coord.copy()

    for x, y in corner:
        coord[x][y] = 2
    
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    end = (itemY, itemX)
    queue = deque()
    queue.append((characterY, characterX))

    # while queue:
    #     x, y = queue.popleft()
    #     if (x, y) == end:
    #         break
    #     for dx, dy in d:
    #         nx, ny = x + dx, y + dy
    #         if (isEdge(matrix, nx, ny) or (nx, ny) in corner) and coord[nx][ny] == 1 and (nx, ny) != (characterY, characterX):
    #             coord[nx][ny] = coord[x][y] + 1
    #             queue.append((nx, ny))

    for a, i in enumerate(coord[:25]):
        for j in i[:25]:
            print("{0:<3}".format(j), end = "")
        print()
    print()
        

    return coord[itemY][itemX]

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)
# %%

# 정답, https://school.programmers.co.kr/questions/48776
from collections import deque

def solution(rectangle,cx,cy,ix,iy):
    candy = set()
    for x,y,X,Y in rectangle:
        candy.update([(j+0.5, i) for j in range(y, Y) for i in (x, X)])
        candy.update([(j,i+0.5) for i in range(x, X) for j in (y, Y)])

    edge = set()
    for b,a in candy:
        for x,y,X,Y in rectangle:
            if x<a<X and y<b<Y:
                break
        else:
            edge.add((b,a))

    que,dy,dx = deque([(0, cy, cx)]), [.5,0,-.5,0], [0,.5,0,-.5]
    while que:
        cnt,b,a = que.popleft()
        if a==ix and b==iy:
            return cnt
        for i in range(4):
            if ((is_in_edge_y:=b+dy[i]), (is_in_edge_x:=a+dx[i])) in edge:
                edge.remove((is_in_edge_y, is_in_edge_x))
                que.append((cnt+1, b+2*dy[i], a+2*dx[i]))
# %%
