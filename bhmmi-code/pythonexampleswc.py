def range_overlap(ranges):
    '''Return common overlap among a set of [low, high] ranges.'''
    lowest = 0.0
    highest = 1.0
    mins = []
    maxs = []
    for (low, high) in ranges:
        maxs.append(high)
        mins.append(low)
    range_thing = (max(mins), min(maxs))
    #print(range_thing)
    for element in ranges:
        if (range_thing[1] >= element[1] and range_thing[0] <= element[0]):
                return None
                print('whoops')
        else:
            return range_thing
            print('yay')
            
x = range_overlap([(1.0,5.0)])
print(x)