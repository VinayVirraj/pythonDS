'''
The idea is to decrease the search space for every iteration compared to linear search.
Binary search makes the search space half for every iter making the time complexity to O(log n)
given a sorted array
'''


def binarySearch(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = int((start+end)/2) # Use this instead of a+b/2 in order to avoid overflow (eg 10^6 + 10^7)
        
        if target > nums[mid]: # if the target is in the second half of the array, move the start pointer
            start = mid + 1
        elif target < nums[mid]: # if the target is in the first half of the array, move the end pointer
            end = mid - 1
        else:
            if target == nums[mid]:
                return mid
    return -1


def recursiveBinarySearch(nums, target, start, end):
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return recursiveBinarySearch(nums, target, start, mid-1)
    else:
        return recursiveBinarySearch(nums, target, mid+1, end)


ex_arr = [-1,0,3,5,9,12]

print(f'Binary search result index: {binarySearch(ex_arr, 9)}')

print(f'Recursive binary search result index: {recursiveBinarySearch(ex_arr, 9, 0, len(ex_arr))}')
