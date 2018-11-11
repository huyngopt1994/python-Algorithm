# https://www.spoj.com/problems/MAKEMAZE/fbclid=IwAR1qCNiAcybrweV9haxuL-auJg99ShNY8jvp2Qg66CHzy0IYFXEW6WLjqng
from copy import deepcopy
def find_path_using_bts(start, end , edges):
    """Just find a path from start to end with edges."""
def build_edges(dots, graph):
    """We have a lot of dots , how"""


    # 2 dot have direct path ,
    #  we they have same col , but ( row +=1)
    # we have same row , but (col +=1)
    copy_dots = deepcopy(dots)
    for dot in copy_dots:
        del copy_dots
        for


t = int(input())
for _ in range(t):
    graph = {}
    edges = []  # just collect
    # first ly need to check
    row, col = list(map(int, input()))
    # we just have 2 dots in border following this logic
    dot_in_borders = []
    dots = []
    for index_r in range(row):
        if index_r in [0, row - 1]:
            # first row
            row_data = input()
            for index_c in range(col):
                if row_data[index_c] == '.':
                    dot_in_borders.append([index_r, index_c])
                    dots.append([index_r, index_c])
                    graph[(index_r, index_c)] = []

        else:
            # the middle row
            row_data = input()
            if row_data[0] == '.':
                dot_in_borders.append([index_r, 0])
            elif row_data[col - 1] == '.':
                dot_in_borders.append([index_r, col - 1])

            for index_c in range(col):
                if row_data[index_c] == '.':
                    dots.append([index_r, index_c])
                    graph[(index_r, index_c)] = []
    if len(dot_in_borders) != 2:
        print('invalid')
    else:
        build_edges(dots, graph)
        find_path_using_bts(start=dot_in_borders[0], end=dot_in_borders[1], edges=dots)
