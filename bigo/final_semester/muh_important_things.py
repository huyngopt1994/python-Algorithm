from collections import defaultdict


def generate_with_case_1(values):
    result = [values]
    for _ in range(2):
        values = list(values)
        values.append(values[0])
        del values[0]
        result.append(values)
    return result

def generate_with_case_2(values):
    result = [values]
    for _ in range(1):
        values = list(values)
        values.append(values[0])
        del values[0]
        result.append(values)
    return result


def get_distinct_plans(my_task, is_good):
    """If we find 2 cases 1 key have duplicate >=3 or 2 keys have duplicate >=2 => print Yes and choose"""
    my_dict = defaultdict(list)

    count_larger_two = 0
    count_larger_three = False
    duplicated_keys = []

    for index, task in enumerate(my_task):
        my_dict[task].append(index + 1)
        if count_larger_two == 2 or count_larger_three:
            is_good = True
            continue
        if len(my_dict[task]) >= 3:
            count_larger_three = True
            duplicated_keys.append(task)
        elif len(my_dict[task]) >= 2:
            count_larger_two += 1
            duplicated_keys.append(task)

    if count_larger_two == 2 or count_larger_three:
        is_good = True

    if not is_good:
        return []
    result = []
    sorted_task = sorted(my_dict.keys())
    if count_larger_three:
        changed_value = generate_with_case_1(my_dict[duplicated_keys[0]])
        for i in range(3):
            custom_result = []
            for u_key in sorted_task:
                if u_key not in duplicated_keys:
                    custom_result.extend(my_dict[u_key])
                else:
                    custom_result.extend(changed_value[i])
            result.append(custom_result)
    elif count_larger_two == 2:
        changed_value_1 = generate_with_case_2(my_dict[duplicated_keys[0]])
        changed_value_2 = generate_with_case_2(my_dict[duplicated_keys[1]])

        for i in range(2):
            custom_result = []
            for u_key in sorted_task:
                if u_key not in duplicated_keys:
                    custom_result.extend(my_dict[u_key])
                elif u_key == duplicated_keys[0]:
                    custom_result.extend(changed_value_1[i])
                elif u_key == duplicated_keys[1]:
                    custom_result.extend(changed_value_2[i])
            result.append(custom_result)

        custom_result = []
        for u_key in sorted_task:
            if u_key not in duplicated_keys:
                custom_result.extend(my_dict[u_key])
            elif u_key == duplicated_keys[0]:
                custom_result.extend(changed_value_1[0])
            elif u_key == duplicated_keys[1]:
                custom_result.extend(changed_value_2[1])
        result.append(custom_result)

    return result


number = input()
while number:
    my_task = map(int, input().split())
    is_good = False
    tasks = get_distinct_plans(my_task, is_good)
    if tasks:
        print('YES')
        for task in tasks:
            print(' '.join(map(str, task)))
    else:
        print('NO')
    number = input()
