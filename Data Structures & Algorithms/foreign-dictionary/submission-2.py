class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj.setdefault(w1[j], set()).add(w2[j])
                    break

        visited = set()  # False=visited, True=current path
        processed = []
        res = []

        def dfs(c):
            visited.add(c)
            for nbr in adj.get(c, set()):
                if nbr in visited:
                    return True
                if nbr in processed:
                    continue
                if dfs(nbr):
                    return True
            
            visited.remove(c)
            processed.append(c)
            res.append(c)
            return False

        for c in adj:
            if c not in processed:
                if dfs(c):
                    return ""
                
        res.reverse()
        return "".join(res)