pos = -1                                         # pos- position, pos=-1 means till now it does not have any position
def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False




list =[5,8,4,6,9,2]
n = 9
if search(list,n):
    print("found at",pos+1)

else:
    print("not found")

