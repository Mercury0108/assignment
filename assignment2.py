def clasify():
    number = int(input('Enter the number of titles: '))
    total = 0
    below = 0
    inrange = 0
    above = 0
    for x in range(number):
        width = int(input('Enter the title width: '))
        total += width
        if width < 98:
            print('Below range')
            below += 1
        elif width <= 102:
            print('In range')
            inrange += 1
        else:
            print('Above range')
            above += 1
    print(f'Total width: {total}')
    return number, total, below, inrange, above
def calculate_average():
    print(f'Average width: {total/number}')
    print(f'Below range: {below}')
    print(f'In range: {inrange}')
    print(f'Above range: {above}')
number, total, below, inrange, above = clasify()
calculate_average()