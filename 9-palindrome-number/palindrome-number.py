class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        else:
            x=str(x)
            test=True
            while len(x)>1 and test:
                if x[0]==x[len(x)-1]:
                    x=x[1:len(x)-1]
                else:
                    test=False
            return len(x)<=1
            

        