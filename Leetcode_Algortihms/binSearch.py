def binSearch(nums, target):
    
    # establish pointers at start and end of list
    left = 0
    right = len(nums)-1

    # while the left ptr is less than or equal to right ptr
    while left <= right:

        # establish a mid ptr and store the val at mid ptr
        mid = (left + right)//2
        current_num = nums[mid]

        # if the val at mid is less than target move left ptr to mid + 1
        # this disregards all the values to the left of the 
        # current left ptr since this is a sorted array 
        # and all of them will meet this condition 
        # no need to search any lower for the target
        if current_num < target:
            left = mid + 1
        
        #same with right ptr 
        elif current_num > target:
            right = mid - 1
        
        #if none of those conditions are met the current number must be the target
        else:
            return mid

    #if the left and right ptrs cross the target does not exist in the array
    return -1


arr = [11, 22, 23, 28, 32, 56, 69, 72]
print(binSearch(arr, target=68))
