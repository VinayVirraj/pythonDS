# This function is to find the minimum among the maximum number of pages that can be allocated for a student from a given array containing pages of each book.

def isvalid(m, n, arr, max_pages_allocation):
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
    
    if (m > n):
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