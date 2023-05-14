from collections import deque

# BFS method definition
def bfs(graph, start, visited):
    
    queue = deque([start]) # use deque library making queue
    visited[start] = True # mark as visited

    while queue: # iterate until queue emptied
        v = queue.popleft() # print an element from queue 
        print (v, end='')
        for i in graph[v]:  # insert nearest element that havent visitied to queue
            if not visited[i]:
                queue.append(i)
                visited[i] = True # change visit status as a True

graph = [
    [], # index[0] will not be used
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9 # mark visit status as False, value: 9 = node input +1

bfs(graph, 1, visited)
