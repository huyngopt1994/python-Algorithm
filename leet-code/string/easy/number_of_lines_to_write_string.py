def number_of_lines(widths, s):
    width=  0
    if len(s) == 0:
        lines = 0
    lines = 1
    for c in s: #O(n)
        w = widths[ord(c)-ord('a')] #0(1)
        width += w
        if width > 100:
            lines += 1
            width = w
    return lines, width


s = input('nhap chuoi string vao :')
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

print (number_of_lines(widths, s))