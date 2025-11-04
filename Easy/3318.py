class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        from collections import Counter
        answer = []
        curr_counter = Counter(nums[:k])
        sorted_freqs = sorted([(key, curr_counter[key]) for key in curr_counter.keys()], key=lambda x: x[1] * 50 + x[0], reverse=True)
        answer.append(sum([val * freq for (val, freq) in sorted_freqs[:x]]))

        for i in range(1, len(nums) - k + 1):
            curr_counter[nums[i - 1]] -= 1
            curr_counter[nums[i + k - 1]] += 1
            sorted_freqs = sorted([(key, curr_counter[key]) for key in curr_counter.keys()], key=lambda x: x[1] * 50 + x[0], reverse=True)
            answer.append(sum([val * freq for (val, freq) in sorted_freqs[:x]]))
        
        return answer
