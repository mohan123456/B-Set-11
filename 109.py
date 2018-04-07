def a( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(a([1,2,-1,1,5,8]))
