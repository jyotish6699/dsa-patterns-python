# optimized version becasue of remove repetation work
# time complexity O(n) and space complexity O(1)

def longestConsecutiveSequence(nums: list) -> int:

    nums_set = set(nums)
    max_length = 0

    for num in nums_set:
        
        if num - 1 in nums:
            continue

        current = num
        count = 1

        while current + 1 in nums_set:
            current += 1
            count += 1

        max_length = max(max_length, count)

    print(max_length)
            
      
    

longestConsecutiveSequence([1,2,3,6,9,8,4,5])