# Approach-4
# frequency key + hashmap
# time complexity - O(nk)
class Solution4:
    def groupAnagrams(self, strs):
        hashmap = {}

        for word in strs:
            count = [0] * 26

            for c in word:
                index = ord(c) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(word)

        return list(hashmap.values())