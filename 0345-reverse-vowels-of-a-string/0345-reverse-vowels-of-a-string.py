class Solution:
    def reverseVowels(self, s: str) -> str:
        Vowels=['a','e','i','o','u','A','E','I','O','U']
        left,right=0,len(s)-1
        
        s_l=[char for char in s]
        while(left<=right):
            flag,rlag=0,0
            if s_l[left] in Vowels:
                flag=1
            if s_l[right] in Vowels:
                rlag=1
            if flag==1 and rlag==1:
                s_l[left],s_l[right]=s_l[right],s_l[left]
                left+=1
                right-=1
            if flag==0:
                left+=1
            if rlag==0:
                right-=1
        return ''.join(s_l)
        