# Build bubble sort

my_list = []


def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            # try to swap if my_list[i] = my_list[j]
            if my_list[i] > my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp

    return my_list

my_list = [9,2,3,1,4,5,2,5]

print(bubble_sort(my_list))

# Apply insertion sort

def selectionSort(alist):
    for i in range(len(alist)):

        # Find the minimum element in remaining
        minPosition = i

        for j in range(i + 1, len(alist)):
            if alist[minPosition] > alist[j]:
                minPosition = j

        # Swap the found minimum element with minPosition
        temp = alist[i]
        alist[i] = alist[minPosition]
        alist[minPosition] = temp
    return alist

def insertion_sort(array):
    for i in range(1,len(array)):
        j = i
        element = array[i]
        while(j>0 and array[j-1] > element):
            array[j] = array[j-1]
            j -=1
        array[j] = element

    return array

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)