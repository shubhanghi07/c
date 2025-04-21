graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
    }
visited=set()
def dfs(visited,graph,data):
    if data not in visited:
        print(data)
        visited.add(data)
        for n in graph[data]:
            dfs(visited,graph,n)

dfs(visited,graph,'A')















