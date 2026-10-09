class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list) #map charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            anagramMap[tuple(count)].append(s)

        return list(anagramMap.values())