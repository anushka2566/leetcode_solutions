class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hm1={}
        hm2={}
        for i in range(len(s)):
            c1=s[i]
            c2=t[i]
            if c1 in hm1:
                if hm1[c1]!=c2:
                    return False
            else:
                hm1[c1]=c2
            if c2 in hm2:
                if hm2[c2]!=c1:
                    return False
            else:
                hm2[c2]=c1
        return True
            
        