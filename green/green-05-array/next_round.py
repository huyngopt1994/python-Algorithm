#http://codeforces.com/contest/158/problem/A
num_student, k_grade = map(int,input().split())

count = 0
# step 1 , get the result
students = list(map(int, input().split()))

for student in students:
    if (student >0 ) and (student>= students[k_grade-1]):
        count +=1
    else:
        break

print(count)