#for(i=1,i++, i<n):
#    element =a[i]
#    j =i
#    while(j>0 and a[j-1] > element)
#       #shift to left
        #a[j] = a[j-1]
#    a[j] = element

def insertion_sort(array):
    for i in range(1,len(array)):
        j = i
        element = array[i]
        while(j>0 and array[j-1] > element):
            array[j] = array[j-1]
            j -=1
        array[j] =  element

    return array

print(insertion_sort([1,5,0,-3,-4,2,5,7,99,11,22,44,33,191,2]))