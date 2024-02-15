'''
Binary search:

gets an ordered array, starts at the middle. If the middle is the target, return
if middle is less iterate only going to the right (Increasing)
if it is more iterate only going to the left (Decreasing)

'''

def BinarySearch(arr, target):
    start = 0
    cap = len(dummy) - 1   
    middle = (cap + start) // 2

    while start <= cap:
        if target == arr[middle]:
            return f"{arr[middle]} is in array!\n\n"
        
        if target > arr[middle]:
            start += 1  # recalculates lowest value to turn search to the right
            middle = (cap + start) // 2

        if target < arr[middle]:
            cap -= 1    # recalculates highest value to turn search to the left
            middle = (cap + start) // 2

    raise ValueError(f"{target} not in Array!")



#I = 5   F  F  F  F  T  F  F
dummy = [1, 2, 3, 4, 5, 6, 7]


print(BinarySearch(dummy, 3)) # Example of value in array
print(BinarySearch(dummy, -2))# Example of value outside of array



