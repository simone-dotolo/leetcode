class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        def count_devices(row):
            count = 0
            for cell in row:
                count += (cell == '1')
            return count

        res = 0
        prev_dev = 0
        for row in bank:
            if curr_dev := count_devices(row):
                res += (curr_dev * prev_dev)
                prev_dev = curr_dev
        
        return res
