class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        # palindrome checker helper function
        def isPali(s, l, r) -> bool:
            while l < r:
                if s[l] != s[r]: return False
            
                l, r = l + 1, r - 1
            return True

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                if isPali(s, start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return res
