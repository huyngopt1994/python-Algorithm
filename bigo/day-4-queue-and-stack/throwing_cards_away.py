# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1876&fbclid=IwAR1CWvI0x4av97YQEtJanSZRQzlBBlDjyP4EjW44CvswuPYbsOuejwH1RHg

# FIFO
my_tests = []
my_input = int(input())
while my_input != 0:
    my_tests.append(my_input)
    my_input = int(input())


def handle_test(number):
    my_queue = [index for index in range(1, number + 1)]
    is_discarded = True
    discarded_cards = []
    while len(my_queue) > 1:
        if is_discarded:
            discarded_cards.append(str(my_queue.pop(0)))
        else:
            my_queue.append(my_queue.pop(0))

        is_discarded = not is_discarded
    if len(discarded_cards):
        print('Discarded cards: {}'.format(', '.join(discarded_cards)))
    else:
        print('Discarded cards:')
    print('Remaining card: {}'.format(my_queue.pop()))


for my_test in my_tests:
    handle_test(my_test)
