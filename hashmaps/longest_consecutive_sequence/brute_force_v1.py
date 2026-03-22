# Brute force 
# time complexity (n**2)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # seq1 = num, num+1, num+2, num+3......
        seq = set()
        
        for i in nums:
            fresh_start = 1
            count = 1
            
            while(i+fresh_start in nums):
                count+=1
                fresh_start+=1

            seq.add(count)

        print(max(seq))
        
        
        





object1 = Solution()
object1.longestConsecutive([100,4,10,11,200,1,3,2])