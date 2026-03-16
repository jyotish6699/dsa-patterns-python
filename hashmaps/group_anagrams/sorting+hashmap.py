# Approach-3
# sorting + hashmap
# idea - canonical representaion 
# time complexity - O(n k logk)
class Solution3:
    def groupAnagrams(self, strs):
        hashmap = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(word)

        return list(hashmap.values())
