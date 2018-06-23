def find_greatest(number,max):
    if number ==0:
        return max
    last_c = number % 10
    if last_c > max:
        max = last_c
    return find_greatest(number//10, max)

a = int(input())
result = find_greatest(abs(a),0)
print(result)
