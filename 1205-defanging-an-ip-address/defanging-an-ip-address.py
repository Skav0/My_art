class Solution:
    def defangIPaddr(self, address: str) -> str:

        st=''
        for i in range(len(address)):
            if address[i]!='.':
                st+=address[i]
            else:
                st+='[.]'
        return st



        