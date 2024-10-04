class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        def find_target(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = left - (left - right) // 2
                
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return mid
            
            return -1
        
        n = len(skill)
        n_teams = n / 2
        total_skill = sum(skill)

        if total_skill % n_teams != 0:
            return -1
        
        team_skill = total_skill / n_teams

        skill.sort()

        teams = []

        while len(skill):
            team = [skill[-1]]
            target = team_skill - team[0]
            index_target = find_target(skill, target)
            if index_target == -1:
                return -1
            team.append(target)
            teams.append(team)
            skill.pop(index_target)
            skill.pop()
        
        res = 0
        for team in teams:
            res += (team[0] * team[1])
        
        return int(res)
