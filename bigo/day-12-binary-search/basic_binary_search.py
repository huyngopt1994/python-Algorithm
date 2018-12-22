def binary_search(my_input, left, right, get_input):
    while left <= right:
        mid = (left + right) // 2
        if get_input == my_input[mid]:
            # We figure out the index we want
            return mid
        elif get_input < my_input[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search_using_recursion(my_input, left, right, get_input):
    if left <= right:
        mid = (left + right) // 2
        if get_input == my_input[mid]:
            return mid
        elif get_input < my_input[mid]:
            right = mid - 1
        else:
            left = mid + 1
        return binary_search_using_recursion(my_input, left, right, get_input) # should return right now
    return -1


if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))  # Default a is a sorted ascending list
    result = binary_search_using_recursion(my_input=a, left=0, right=n - 1, get_input=x)
    print(result)
