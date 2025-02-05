class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first,second=0,0
        num_diff=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                num_diff+=1
                if num_diff>2:
                    return False
                elif num_diff==1:
                    first=i
                else:
                    second=i
        return (s1[first]==s2[second] and s1[second]==s2[first])
        