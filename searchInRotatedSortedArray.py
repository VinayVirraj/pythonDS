from inputs import takeArrInput

'''
when given with a sorted array (asc order) think of applying binary search. Idea is if binary search 
algorithm is applied on the rotated sorted array, one between the two halves will be sorted
'''

def searchSortedArr(nums, target):
    start = 0
    end = len(nums) - 1
    i = 1
    while start <= end:
        print(f"\n/////////// iter {i} ///////////")
        print(f"Given list {nums}")
        print(f"Given target {target}")
        mid = start + (end - start) // 2
        print(f"start_idx = {start}, end_idx = {end}, mid_idx = {mid}")
        if nums[mid] ==  target:
            print(f"final mid aka the answer {mid}\n")
            return mid
        elif nums[start] <= nums[mid]: # first half of the array
            print(f"Checking if start ({nums[start]}) is less than or equal to curr mid ({nums[mid]})")
            if nums[start] <= target < nums[mid]: # if the target is in the first half
                print(f"Checking if the target is in between the start ({nums[start]}) and the curr mid ({nums[mid]})")
                end = mid - 1
                print("yes it is")
            else:
                print(f"Target is not between the start ({nums[start]}) and the curr mid ({nums[mid]}) so we move start pointer")
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]: # if the target is in the second half
                print(f"Checking if the target is in between the curr mid ({nums[mid]}) and end ({nums[end]})")
                start = mid + 1
                print("yes it is")
            else:
                print(f"Target is not between the curr mid ({nums[mid]}) and end ({nums[end]}) so we move end pointer")
                end = mid - 1
        i += 1 # just to know the iteration (not used in the function)
    return -1


ex_arr = [6, 7, 0, 1, 2, 3, 4, 5]

print(f'\nThis is an example =====================================>>')
searchSortedArr(ex_arr, 5)

while True:
    inp_from_user = takeArrInput()
    if len(inp_from_user) == 1 and inp_from_user[0] == 911:
        print("Exiting ......")
        break

    if inp_from_user:
        value = int(input("Enter the value for which the index is needed: "))
        print(f'\nYour Array : {inp_from_user} \nindex of {value} is : {searchSortedArr(inp_from_user, value)}\n')