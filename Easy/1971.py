class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj = [[] for i in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def bfs(s,d):

            level = {s:0}
            parent = {s:None}
            frontier = [s]
            i = 1
            while (frontier != []):
                next = []
                for v in frontier:
                    for u in adj[v]:
                        if(u not in level):
                            level[u] = i
                            parent[u] = v
                            next.append(u)
                    frontier = next
                    i += 1

            return d in level
        
        return bfs(source,destination)