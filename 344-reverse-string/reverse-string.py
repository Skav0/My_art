class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ch=''
        for i in range(len(s)):
            ch+=s[i]
        ch=ch[::-1]
        for i in range(len(ch)):
            s[i]=ch[i]

        