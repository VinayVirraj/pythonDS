from inputs import takeInputAllocateMinPages

# This function is to find the minimum among the maximum number of pages that can be allocated for a student from a given array containing pages of each book.

def isvalid(m, n, arr, max_pages_allocation):
    '''
    This function is used to check if a mid value is valid or not. Based on this
    left or right half of the array is chosen to reduce the time complexity to log n.
    '''
    student_no = 1
    pages = 0
    for i in range(n):
        if (arr[i] > max_pages_allocation): # if current array value (number of pages in a book) > current mid value (max number of pages that can be allocated)
            print(f"Mid value is invalid because current array value is greater than mid value")
            return False
        if (pages + arr[i] <= max_pages_allocation):
            pages += arr[i]
            print(f"current sum of pages is: {pages}, max pages can be allocated is: {max_pages_allocation}")
        else:
            student_no += 1
            pages = arr[i]   # if adding current array value (number of pages) to the pages is exceeding the max_pages_allocation then get a new student and start assigning from here
            print(f"current number of students: {student_no}")
        if (student_no > m):
            print(f"Mid value is invalid because current number of students {student_no} is already greater than given number of students {m}")
            return False
    return True


def findPages(n ,arr ,m):
    '''
    arr: array containing pages of each book
    n: number of books
    m: number of students
    '''
    if (m > n):         # number of students > number of books..... not possible to solve the problem
        return -1
    start = 0           # make the start and end to be the minimum and maximum of the total pages possible
    end = sum(arr)
    answer = -1
    i = 1
    while (start<=end):
        print(f"\n/////////// iter {i} ///////////")
        print(f"start is : {start}")
        print(f"end is : {end}")
        mid = start + (end - start) // 2
        print(f"mid value is : {mid}")
        if (isvalid(m, n, arr, mid)):
            print(f"mid value is valid..so current answer is {mid}")
            answer = mid
            print("moving end.............")
            end = mid - 1
        else:
            print("mid value is invalid")
            print("moving start...........")
            start = mid + 1
        i += 1 # just to know the iteration (not used in the function)
    return answer

while True:
    n, arr, m = takeInputAllocateMinPages()
    print(f'\nYour Book Array : {arr}')
    findPages(n, arr, m)