class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts={}
        for i in strs: #n
            b="".join(sorted(i)) #sorted klogk
            if b in counts:
                counts[b].append(i)
            else:
                counts[b]=[i]
        return list(counts.values())

#time = o(n.klogk)
#space = o(n)
        

        
        