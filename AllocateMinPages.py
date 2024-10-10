# This function is to find the minimum among the maximum number of pages that can be allocated for a student from a given array containing pages of each book.

def isvalid(m, n, arr, max_pages_allocation):
    '''
    This function is used to check if a mid value is valid or not. Based on this
    left or right half of the array is chosen to reduce the time complexity to log n.
    '''
    student_no = 1
    pages = 0
    for i in range(n):
        if (arr[i] > max_pages_allocation):
            return False
        if (pages + arr[i] <= max_pages_allocation):
            pages += arr[i]
        else:
            student_no += 1
            pages = arr[i]
        if (student_no > m):
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
    start = 0
    end = sum(arr)
    answer = -1
    while (start<=end):
        mid = start + (end - start) // 2
        
        if (isvalid(m, n, arr, mid)):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
        
    return answer