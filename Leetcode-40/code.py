class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], res)
        return res
    
    def backtrack(self, candidates, target, start, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            self.backtrack(candidates, target-candidates[i], i+1, path+[candidates[i]], res)