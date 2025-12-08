class Solution:
    def reverseWords(self, s: str) -> str:

             
        
        
        s=s+' '

        ch=''
        while s!='':

            ind=s.find(' ')
            ch+=s[:ind][::-1]+' '
            
            s=s[ind+1:len(s)]



        return ch[:len(ch)-1]




