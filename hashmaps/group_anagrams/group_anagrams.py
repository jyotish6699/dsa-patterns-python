# Approach-1: Brute force(compare every pair), time complexity O(n**2*k logk)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        visited = [False] * len(strs)
        result = []

        for i in range(len(strs)):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):

                if visited[j]:
                    continue

                if sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    visited[j] = True
            result.append(group)

        print(result)

brute_force = Solution()
brute_force.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


# Approach-2
# Brute force + charactere frequency
# comparision pair using frequency
# time complexity = O(n**2 * k)
class Solution2:
    def groupAnagrams(self, strs):
        
        def is_anagrams(a,b):  # a,b = string(word)
            if len(a) != len(b):
                return False
            
            count = [0] * 26

            for c in a:
                index = ord(c) - ord('a')
                count[index] += 1

            for c in b:
                index = ord(c) - ord('a')
                count[index] -= 1

            for x in count:
                if x != 0:
                    return False
            
            return True
        
        visited = [False] * len(strs)
        result = []

        for i in range(len(strs)):

            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i+1, len(strs)):
                if visited[j]:
                    continue

                if is_anagrams(strs[i], strs[j]):
                    group.append(strs[j])
                    visited[j] = True
            
            result.append(group)

        return result


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