def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    increasing = True
    decreasing = True

    for i in range(1,len(lst)):
        

        if lst[i] < lst[i-1]:
            decreasing = False
        if lst[i] > lst[i-1]:
            increasing = False
        
    return increasing or decreasing

list1 = [1,2,3,4,5]
list2 = [10,9,8,7,6]
list3 = [4,7,2,4,9]

print(monotonic(list1))
print(monotonic(list2))
print(monotonic(list3))