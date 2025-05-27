class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, total):
            if total == target:
                res.append(path[:])
                return
            
            if i == len(candidates) or total > target:
                return
            
            # add
            path.append(candidates[i])
            dfs(i, path, total + candidates[i])

            # don't
            path.pop()
            dfs(i + 1, path, total)

        dfs(0, [], 0)
        return res
        