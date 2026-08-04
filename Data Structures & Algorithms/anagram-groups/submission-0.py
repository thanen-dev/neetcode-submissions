class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        box = {}
        for word in strs:
            key = tuple(sorted(word))

            if key in box:
                box[key].append(word)
            else:
                box[key] = [word]

        return list(box.values())