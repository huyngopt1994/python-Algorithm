s = int(input())
height = 0
num_current_height =1
def get_current_heigh(index):
    count = 0
    for i in range(index+1):
        count +=i
    return count
while s >=0:
    s -= get_current_heigh(height+1)
    height +=1

print(height-1)