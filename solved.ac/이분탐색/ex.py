
#반복문
def binarySearch(array,start,end,k):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==k:
            return mid
        elif array[mid]>k:
            end=mid-1
        else:
            start=mid+1
    else:
        return False