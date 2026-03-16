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
