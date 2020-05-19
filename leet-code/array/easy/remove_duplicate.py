"""https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/"""
def removeduplicate(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i +=1
            nums[i] = nums[j]

    return (i+1)

# i =0 ; j =1 => j ->> when we got a[j] != a[i] => got the new  => nums[i] = nums[j]
a = [0,0,1,1,1,2,2,3,3,4]

print(removeduplicate(a))
print(a)
