class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def is_solution(graph,path):
            return path != [] and (path[-1] == len(graph)-1)

        def make_move(position,path):
            path.append(position)

        def unmake_move(path):
            path.pop()

        def solve(graph,position,res,path):

            make_move(position,path)

            if(is_solution(graph,path)):
                res.append(path.copy())
            else:
                for next_move in graph[position]:
                    solve(graph,next_move,res,path)
                    
            unmake_move(path)

            return res

        path = []
        res = []

        solve(graph,0,res,path)

        return res
            


            