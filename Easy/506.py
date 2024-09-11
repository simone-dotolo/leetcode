class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        sorted_score = sorted(score, reverse=True)
        score_place_dict = {score : place for place, score in enumerate(sorted_score)}

        ans = [str(score_place_dict[i]+1) for i in score]

        for i in range(len(ans)):
            if ans[i] == '1':
                ans[i] = 'Gold Medal'
            elif ans[i] == '2':
                ans[i] = 'Silver Medal'
            elif ans[i] == '3':
                ans[i] = 'Bronze Medal'

        return ans