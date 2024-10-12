'''M cows needs to placed in N stalls such that cows are seperated by the maximum of (minimum distance possible in each case cows can be placed in the stalls).
Stall positions are provided in an array'''
from inputs import takeInputAggrCows

def isValid(arr, M, N, mid):
    
    c = 1
    last_stall_pos = arr[0]
    for i in range(1, N):
        if (arr[i] - last_stall_pos >= mid):
            c += 1
            last_stall_pos = arr[i]
        if c == M:
            return True
    return False


def AggrCows(arr, M, N):
    sorted_arr = sorted(arr)
    print(f"\nArray in sorted order : {sorted_arr}")
    st = 1                                          # Atleast two cows will be there so min distance will be 1
    end = sorted_arr[N-1] - sorted_arr[0]           # At least two cows will be there so max distance will be max - min
    ans = -1
    while (st <= end):
        mid = st + (end - st)//2
        print(f"start: {st}, end: {end}, mid: {mid}")
        if (isValid(sorted_arr, M, N, mid)):        # if the mid value is valid i.e cows can be arranged using this min distance(mid)
            print(f"Mid value {mid} is valid (place cows apart by a min distance of {mid} is possible), updating start")
            ans = mid
            st = mid + 1                            # update start to check in the right part of the array for a larger distance
        else:
            print(f"Mid value {mid} is invalid (cannot place cows apart by a min distance of {mid}), updating end")
            end = mid - 1  
    return ans

N, arr, cows = takeInputAggrCows()

print(AggrCows(arr, cows, N))
