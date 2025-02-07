class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        from collections import Counter
        nodes = Counter()
        labels = Counter()
        distinct_colors = 0
        ans = []
        for query in queries:
            node, label = query
            if nodes.get(node, 0) == 0:            
                if labels.get(label, 0) == 0:
                    distinct_colors += 1
                nodes[node] = label
                labels[label] += 1
            else:
                prev_label = nodes[node]
                labels[prev_label] -= 1
                if labels[prev_label] == 0:
                    distinct_colors -= 1
                if labels.get(label, 0) == 0:
                    distinct_colors += 1
                nodes[node] = label
                labels[label] += 1
            ans.append(distinct_colors)
        return ans
