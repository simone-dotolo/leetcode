class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        arriveAlice = sum(days_per_month[:int(arriveAlice.split('-')[0])-1]) + int(arriveAlice.split('-')[1])
        leaveAlice = sum(days_per_month[:int(leaveAlice.split('-')[0])-1]) + int(leaveAlice.split('-')[1]) 
        arriveBob = sum(days_per_month[:int(arriveBob.split('-')[0])-1]) + int(arriveBob.split('-')[1]) 
        leaveBob = sum(days_per_month[:int(leaveBob.split('-')[0])-1]) + int(leaveBob.split('-')[1])

        return max(min(leaveAlice, leaveBob) - max(arriveAlice, arriveBob) + 1, 0)
