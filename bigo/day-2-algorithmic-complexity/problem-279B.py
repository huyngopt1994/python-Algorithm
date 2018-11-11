# http://codeforces.com/problemset/problem/279/B
n_books, n_time_reading = list(map(int, input().split()))

minutes = list(map(int, input().split()))


def get_max_with_o_n_2():
    my_max = 0
    for i in range(n_books):
        total = 0
        count = 0
        for j in range(i, n_books):
            total += minutes[j]
            if total <= n_time_reading:
                count += 1
            else:
                break
        if count == n_books:
            return n_books
        if count >= my_max:
            my_max = count
    return my_max


def get_the_first_array(n_books, n_time_reading, minutes):
    first_count = 0
    first_value = 0
    for i in range(n_books):
        first_value += minutes[i]
        if first_value <= n_time_reading:
            first_count += 1
        else:
            return [i - 1, first_count, first_value - minutes[i]]
    return [n_books, first_count, first_value]


def get_max_with_o_n(n_books, n_time_reading, minutes):
    if n_books == 1:
        if minutes[0] <= n_time_reading:
            return 1
        else:
            return 0
    j, first_count, first_value = get_the_first_array(n_books, n_time_reading, minutes)
    my_max = first_count

    if my_max == n_time_reading:
        return my_max
    for i in range(1, n_books):

        first_value -= minutes[i - 1]
        first_count -= 1
        j += 1
        while j <= n_books - 1:
            first_value += minutes[j]
            if first_value <= n_time_reading:
                j += 1
                first_count += 1
            else:
                first_value -= minutes[j]
                j -= 1
                break
        if first_count > my_max:
            my_max = first_count
    return my_max


print(get_max_with_o_n(n_books, n_time_reading, minutes))
