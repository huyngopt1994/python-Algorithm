def printReserve(content):
    if len(content) == 1:
        print(content)
        return
    printReserve(content[1:])
    print(content[0])


printReserve('chao')
