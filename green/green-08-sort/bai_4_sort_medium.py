class Student(object):
    def __init__(self, name, avg, code):
        self.name = name
        self.avg = avg
        self.code = code


number = int(input())
students = []
for _ in range(number):
    name = input()
    code, math, lit = input().split()
    avg = (float(math) + float(lit)) / 2
    student = Student(name, avg, code)
    students.append(student)


# After that we got

def sort_bubble(students):
    for i in range(len(students) - 1):
        for j in range(i + 1, len(students)):
            # first we will sort folllowing the avg
            if students[i].avg > students[j].avg:
                # Please swap this
                temp = students[i]
                students[i] = students[j]
                students[j] = temp

                students[i], students[j] = students[j], students[i]
            elif students[i].avg == students[j].avg:
                # please swap following code
                if students[i].code > students[j].code:
                    # Please swap student
                    temp = students[i]
                    students[i] = students[j]
                    students[j] = temp
    return students


students = sort_bubble(students)
for student in students:
    student_string = ' '.join([student.code, student.name])
    print(student_string)
