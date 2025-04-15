class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_list=[word for word in word1]
        word2_list=[word for word in word2]
        l1=len(word1_list)
        l2=len(word2_list)
        minlen=l1 if l1<l2 else l2
        new=[]
        for i in range(minlen):
            new.append(word1_list[i])
            new.append(word2_list[i])
        if l1>minlen:
            for i in range(minlen,l1):
                new.append(word1_list[i])
        if l2>minlen:
            for i in range(minlen,l2):
                new.append(word2_list[i])
        return ''.join(item for item in new)