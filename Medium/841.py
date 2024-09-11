class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = [0]
        frontier = [key for key in rooms[0]]

        while(frontier != []):
            next = []
            for room in frontier:
                if(room not in visited):
                    visited.append(room)
                    for key in rooms[room]:
                        if(key not in visited):
                            next.append(key)
            frontier = next
            
        return len(visited) == len(rooms)