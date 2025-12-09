class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        o=operations
        X=0
        for i in range(len(o)):
            if o[i]=='X--' or o[i]=='--X':
                X-=1

            else:
                X+=1
        return X
        