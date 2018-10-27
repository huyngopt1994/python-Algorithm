number = int(input())
numbers = list(map(int, input().split()))


def is_odd(number):
    # check so le
    if number % 2 != 0:
        return True
    else:
        return False


def bubble_sort(numbers):

    for i in range(len(numbers) - 1):
        if is_odd(numbers[i]):
            i_odd = True
        else:
            i_odd = False
        for j in range(i+1, len(numbers)):
            if i_odd:
                # handle odd number
                # Descending
                if is_odd(numbers[j]):
                    # swap them
                    if numbers[i] < numbers[j]:
                        numbers[i], numbers[j] = numbers[j], numbers[i]
            else:
                if not is_odd(numbers[j]):
                    # ascending
                    if numbers[i] > numbers[j]:
                        numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

numbers = bubble_sort(numbers)

numbers_string = ' '.join(map(str,numbers))
print(numbers_string)
