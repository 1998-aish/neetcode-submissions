class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts={}
        for i in strs:
            b="".join(sorted(i))
            if b in counts:
                counts[b].append(i)
            else:
                counts[b]=[i]
        return list(counts.values())


        

        
        