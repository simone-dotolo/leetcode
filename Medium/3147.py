class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(len(energy) - 1, -1, -1):
            if i - k >= 0:
                energy[i - k] += energy[i]
        return max(energy)
