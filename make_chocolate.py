def make_chocolate(small, big, goal):
    if big > 0:
        big *= 5
    if goal - big < small:
        small = goal - big
        print(small)
        return small
    else:
        print('-1')
        return -1


make_chocolate(4,1,9)
