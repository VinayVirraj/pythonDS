# This function is to find the minimum of the maximum number of pages that can be allocated for a student from a given array of pages of each book.

def findPages(self,n ,arr ,m):
        start = 0
        end = sum(arr)
        pages = 0
        while (start <= end):
            mid = start + (end - start)/2
            st = 1
            for i in range(n):
                # add a condition here to verify if the condition is valid to iterate through the remaining array
                if arr[i] + pages <= mid:
                    pages += arr[i]
                else:
                    st += 1
                    pages = arr[i]
