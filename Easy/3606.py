class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        categories = {'electronics': [], 'grocery': [], 'pharmacy': [], 'restaurant': []}
        valid = []

        n = len(code)
        for i in range(n):
            if isActive[i] and businessLine[i] in categories.keys() and code[i].replace('_', '0').isalnum():
                categories[businessLine[i]].append(code[i])
        
        for category in categories:
            valid.extend(sorted(categories[category]))
        
        return valid
