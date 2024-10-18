
def takeArrInput():
    try:
        return list(map(int, input("Enter your list separated by spaces or type 911 to quit: ").split()))
    except:
        print('\nEnter a valid list')


def takeInputAllocateMinPages():
    try:
        l = []
        n = int(input("\nEnter number of books: "))
        for i in range(n):
            pages = int(input(f"Enter number of pages for book {i+1}: "))
            l.append(pages)
        m = int(input("Enter the number of students: "))
        return n, l, m
    except:
        print('\nEnter valid values only')


def takeInputAggrCows():
    try:
        l = []
        n = int(input("\nEnter number of stalls: "))
        for i in range(n):
            stalls = int(input(f"Enter order number of stall {i+1}: "))
            l.append(stalls)
        m = int(input("Enter the number of Cows: "))
        return n, l, m
    except:
        print('\nEnter valid values only')
