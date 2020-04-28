def sort(nums):
    for i in range(len(nums)-1):
        minpos=i
        for j in range(i, len(nums)):
            if nums[minpos] > nums[j]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp




nums=[23,12,45,132,16,78,90]
sort(nums)
print(nums)



