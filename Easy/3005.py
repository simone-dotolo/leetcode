class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = [0 for _ in range(100)]
        for num in nums:
            freqs[num - 1] += 1
        
        max_freq = max(freqs)
        count_max_freq = 0
        res = 0
        for freq in freqs:
            res += (freq == max_freq) * freq
        return res
