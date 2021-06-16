# : searching for a value using Binary Search

def binarysearch(array, target_value):
    return binarysearchhelper(array, target_value, 0, len(array)-1)


def binarysearchhelper(array, target_value, left, right):
    if left > right:
        return -1
    middle = (left + right)//2
    predictedvalue = array[middle]
    if target_value == predictedvalue:
        return middle
    elif target_value < predictedvalue:
        return binarysearchhelper(array, target_value, left, middle - 1)
    else:
        return binarysearchhelper(array, target_value, middle +1, right)


