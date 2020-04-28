pos = -1                                         # pos - position, pos=-1 means till now it does not have any position
def search(list,n):
    low = 0
    u = len(list)-1
    while low <= u:
        mid = (low + u) // 2
        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid]< n:
                
                low = mid+1
            else:
                u = mid-1


    return False




list =[2,3,45,67,78,190,2340,50089]

n = 2


if search(list, n):
    print("found at", pos+1)

else:
    print("not found")

