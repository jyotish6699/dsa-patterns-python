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

