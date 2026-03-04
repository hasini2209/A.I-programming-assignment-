from collections import deque
def bfs():
visited = set()
queue = deque([(0,0)])
while queue:
state = queue.popleft()
a,b = state
print(state)
if a == 2:
print("Goal reached:"
, state)
return
if state in visited:
continue
visited.add(state)
next
_
states = [
(4,b), # fill A
(a,3), # fill B
(0,b), # empty A
(a,0), # empty B
(max(0,a-(3-b)), min(3,a+b)), # pour A→B
(min(4,a+b), max(0,b-(4-a))) # pour B→A
]
for s in next
_
states:
if s not in visited:
queue.append(s)
bfs()