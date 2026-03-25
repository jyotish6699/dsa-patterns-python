# Brute force but with fast lookup using set 
# tradeoff memory -> speed using hashing
# timecomplexity still O(n**2) but inner cost reduce to O(1)

def longestConsecutiveSequence(nums: list[int]):
    seq = set()

    for i in nums:
        fresh_start = 1
        count = 1
        while(i+fresh_start in set(nums)):
            count += 1
            fresh_start +=1

        seq.add(count)
    print(max(seq))

longestConsecutiveSequence([2,3,4,8,5,10])

