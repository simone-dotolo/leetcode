class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        from itertools import permutations

        # Uber-spaghetti
        digits = {str(n_digits): [[n_digits] * n_digits] for n_digits in range(1, 8)}

        for i in range(1, 5):
            for j in range(i, 8 - i):
                for k in range(0, j - 1):
                    if len(set([i, j, k])) == 3 and i + j + k < 8:
                        new_digits = [i] * i + [j] * j + [k] * k
                        digits[str(i+j+k)].append(new_digits)

        candidates = digits[str(len(str(n)))]
        if len(str(n)) < 7:
            candidates += digits[str(len(str(n)) + 1)]
        
        permuted_candidates = []

        for candidate in candidates:
            candidate_permutations = list(set(permutations(candidate)))
            for candidate_permutation in candidate_permutations:
                permuted_candidates.append(int(''.join([str(digit) for digit in candidate_permutation])))

        permuted_candidates.sort()

        for el in permuted_candidates:
            # Could be a binary search
            if el > n:
                return el
