number_cubes = int(input())
max_level_cube  = 0
used_cubes =0
while (used_cubes<=number_cubes):
    max_level_cube +=1
    used_cubes += max_level_cube

# we subtract 1 to get the right max_level_cube
max_level_cube -= 1

print(max_level_cube)