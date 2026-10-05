class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for x in s:
            if sdict.get(x) == None:
                sdict[x] = 1
            else:
                sdict[x] += 1

        for y in t:
            if tdict.get(y) == None:
                tdict[y] = 1
            else:
                tdict[y] += 1

        print (sdict)
        print (tdict)
        return sdict == tdict