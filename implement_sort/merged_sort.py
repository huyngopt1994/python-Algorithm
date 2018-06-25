"""
O(n) = nlogn
steps:
mergesort(arr[],l,m)
step1 :
if l > m
{
1./ Fin the middle of this array
m =(e+s)//2
2./ Call the merge sort for the first half
Call mergesort(arr,l ,m)
3./ call mergesort for second half
    call mergesort(arr,m+1,r)
4./ merge the two halves sorted in step2 and step3:
    call merge(arr,l,m,r)
    }
"""
#complete merge fucntionality firstly

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
        element = arr[i]
        while(j>0 and arr[j-1] > element):
            arr[j] = arr[j-1]
            j -=1
        arr[j] = element
    return arr

def merge_version2(arr,l,m,r):
    """
    :param arr1: 1st unsorted array
    :param arr2: 2nd unsorted array
    :return: new array
    """
    arr1 = arr[l:m+1]
    arr2 = arr[m+1:r+1]
    new_array = []
    j = 0
    i =0
    k = l
    #we failed because some time two list is not same
    while(j < len(arr1)) and (i < len(arr2)):
            if arr1[j] < arr2[i]:
                new_array.append(arr1[j])
                j +=1
            else:
                new_array.append(arr2[i])
                i +=1
    while(j< len(arr1)):
        new_array.append(arr1[j])
        j+=1

    while (i < len(arr2)):
        new_array.append(arr2[i])
        i+=1

    #for i in new_array:
    #    arr[k] =i
    #    k+=1
    arr[l:r+1] = new_array

def merge(arr, l, m, r):
    L =arr[l:m+1]
    R = arr[m+1:r+1]
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l,r):
    if l<r:
        m = (l+(r))//2
        # merge sort for first half
        merge_sort(arr,l,m)
        # merge sort for second half
        merge_sort(arr, m+1, r)

        merge_version2(arr, l,m,r)



my_list = [1,2,43,1,-2,4,-1,99,101,-5,2,3,5,1,10,11,23,55,122,85,-23232,11,44,66,88,99,2323,11,3232,-545454,1,4,6,2,76]
print(len(my_list))
merge_sort(my_list,0,len(my_list)-1)
print(my_list)
print(len(my_list))