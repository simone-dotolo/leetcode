class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([(-1) ** ('-' in op) for op in operations])
