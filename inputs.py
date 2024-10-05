
def takeArrInput():
    try:
        return list(map(int, input("Enter your list separated by spaces or type 911 to quit: ").split()))
    except:
        print('\nEnter a valid list')