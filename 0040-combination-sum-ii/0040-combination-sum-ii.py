class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target:
                return
            
            # build paths
            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # add to paths
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                
                # skip combo
                path.pop()
            
        backtrack(0,[], 0)
        return res
