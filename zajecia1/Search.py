import sys, time
from collections import deque
 
D = {'┼': 'udrl', '│': 'ud', '─': 'rl', ' ': '', '┐': 'dl', '┘': 'ul', '└': 'ur', '┌': 'dr',
     '┤': 'udl', '┴': 'url', '├': 'udr', '┬': 'drl', '╵': 'u', '╷': 'd', '╴': 'l', '╶': 'r'}
M = {'u': (-1, 0, 'd'), 'd': (1, 0, 'u'), 'r': (0, 1, 'l'), 'l': (0, -1, 'r')}
 
lines = open(sys.argv[1], encoding='utf-8').read().rstrip('\n').split('\n')
w = max(len(l) for l in lines)
g = [l.ljust(w) for l in lines]
h = len(g)
 
def show(s=None, e=None, vis=(), q=()):
    out = ['\033[H\033[J']
    for y in range(h):
        for x in range(w):
            p = (y, x)
            c = '31' if p == s else '34' if p == e else '33' if p in q else '32' if p in vis else ''
            out.append(f'\033[1;{c}m{g[y][x]}\033[0m' if c else g[y][x])
        out.append('\n')
    print(''.join(out))
 
show()
sx, sy = map(int, input('Start (x y): ').split())
ex, ey = map(int, input('Koniec (x y): ').split())
alg = input('Algorytm (BFS/DFS): ').strip().upper()
s, e = (sy, sx), (ey, ex)
 
q = deque([s])
vis = set()
steps = 0
found = False
while q:
    p = q.popleft() if alg == 'BFS' else q.pop()
    if p in vis:
        continue
    vis.add(p)
    steps += 1
    if p == e:
        found = True
        break
    for d in D.get(g[p[0]][p[1]], ''):
        dy, dx, o = M[d]
        n = (p[0] + dy, p[1] + dx)
        if 0 <= n[0] < h and 0 <= n[1] < w and o in D.get(g[n[0]][n[1]], '') and n not in vis and n not in q:
            q.append(n)
    show(s, e, vis, q)
    time.sleep(0.1)
 
show(s, e, vis, q)
print('Znaleziono ścieżkę' if found else 'Brak ścieżki')
print('Kroki:', steps)
