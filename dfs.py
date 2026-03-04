def dfs(state, visited):
if state in visited:
return
print(state)
visited.add(state)
a,b = state
if a == 2:
print("Goal reached:"
, state)
return
next
_
states = [
(4,b),
(a,3),
(0,b),
(a,0),
(max(0,a-(3-b)), min(3,a+b)),
(min(4,a+b), max(0,b-(4-a)))
]
for s in next
_
states:
dfs(s, visited)
dfs((0,0), set())