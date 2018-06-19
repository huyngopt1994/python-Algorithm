s = int(input())
height = 0
def need_cubes_for_index(index):
    count = 0
    for i in range(index+1):
        count +=i
    return count

while s >=0:
    height += 1
    s -= need_cubes_for_index(height)

print(height-1)