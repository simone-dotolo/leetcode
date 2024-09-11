class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        mask = [0 for _ in range(len(hand))]
        hand.sort()

        while sum(mask) != len(hand):
            count = 0
            last_card = 0
            i = 0
            while i < len(hand) and count < groupSize:
                if count == 0 and mask[i] == 0:
                    last_card = hand[i]
                    count += 1
                    mask[i] = 1
                elif mask[i] == 0 and hand[i] == last_card + 1:
                    last_card = hand[i]
                    count += 1
                    mask[i] = 1
                i += 1
            if count != groupSize:
                return False
                
        return True