class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        

    def add(self, val: int) -> int:
        found = False
        for i, num in enumerate(self.nums):
            if val < num:
                self.nums.insert(i, val)
                found = True
                break
        if not found:
            self.nums.append(val)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)