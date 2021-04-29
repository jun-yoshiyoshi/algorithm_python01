# ABC007 C問題
from collections import deque
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

grid = [input() for _ in range(r)]

q = deque()
q.append((sy, sx))

INF = 1 << 60
dist = [[False for _ in range(c)] for _ in range(r)]
dist[sy][sx] = 0

# 右へ移動したとき、下へ移動したとき、左へ移動したとき、上へ移動したとき、それぞれの座標の変動
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

while (len(q) > 0):
    now = q.popleft()
    y, x = now

    for di in range(4):
        ny = y + dy[di]
        nx = x + dx[di]

        if (ny < 0 or ny >= r or nx < 0 or nx >= c):
            continue
        if (grid[ny][nx] == "#"):
            continue
        if (dist[ny][nx] != False):
            continue

        dist[ny][nx] = dist[y][x]+1
        q.append((ny, nx))

# for i in range(r):
#    for j in range(c):
#        print(dist[i][j], end="")
#    print()

print(dist[gy][gx])
