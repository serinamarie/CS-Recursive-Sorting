# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    left_index = 0
    right_index = 0

    merged_arr = []
    
    while left_index < len(arrA) and right_index < len(arrB):
        if arrA[left_index] > arrB[right_index]:
            merged_arr.append(arrB[right_index])
            right_index = right_index + 1

        elif arrA[left_index] < arrB[right_index]:
            merged_arr.append(arrA[left_index])
            left_index = left_index + 1
    while right_index < len(arrB):
        merged_arr.append(arrB[right_index])
        right_index = right_index + 1
    while left_index < len(arrA):
        merged_arr.append(arrA[left_index])
        left_index = left_index + 1
        

    return merged_arr

arr1 = [9,8,7]
arr2 = [6,5,4]
print(merge(arr1,arr2))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2
    left_side = arr[:midpoint]
    right_side = arr[midpoint:]
    return merge(merge_sort(left_side), merge_sort(right_side))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
