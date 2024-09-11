class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets_to_buy = tickets[k]
        res = 0
        count = 0
        for i, ticket in enumerate(tickets):
            if ticket < tickets_to_buy:
                res += ticket
            else:
                res += tickets_to_buy
                count += i > k
        
        return res - count
