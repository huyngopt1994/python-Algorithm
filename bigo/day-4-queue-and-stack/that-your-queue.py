# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3359
# # This wrong way , I will create a new solution following the instruction
def handle_process(populate, commands):
    my_queue = [i for i in range(1, populate + 1)]
    result = []
    my_urgents = []
    is_insert = False
    for command in commands:
        if command[0] == 'N':
            person = my_queue.pop(0)
            if not is_insert:
                while person in my_urgents:
                    my_urgents.remove(person)
                    person = my_queue.pop(0)

            result.append(person)
            my_queue.append(person)
            is_insert = False
        else:
            # if error , we just create a new queue with first is error ,and move c
            urgent = int(command[1])
            if urgent != my_queue[0]:
                is_insert = True
                my_queue.insert(0, urgent)
                my_urgents.append(urgent)

            continue
    return result


populate, number_of_command = list(map(int, input().split()))
index = 1
while populate:
    commands = []
    for _ in range(number_of_command):
        commands.append(list(input().strip().split()))
    result = handle_process(populate, commands)
    print('Case {}:'.format(index))
    for item in result:
        print(item)
    populate, number_of_command = list(map(int, input().split()))
    index += 1
