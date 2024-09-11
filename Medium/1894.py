class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        sum_of_chalks = sum(chalk)

        last_iteration_k = k % sum_of_chalks

        for i, ch in enumerate(chalk):
            if ch <= last_iteration_k:
                last_iteration_k -= ch
            else:
                return i
        
        return len(chalk) - 1