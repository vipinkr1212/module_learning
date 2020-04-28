def sort(nums):
    for i in range(0,len(nums)):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1] =temp




nums=[23,12,45,132,16,78,90]
sort(nums)
print(nums)



