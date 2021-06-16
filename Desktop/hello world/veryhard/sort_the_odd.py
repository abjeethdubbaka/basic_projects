
#You will be given an array of numbers. Y
# ou have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# def sort_array(arr):
#   odds = sorted((x for x in arr if x%2 != 0), reverse=True)
#   return [x if x%2==0 else odds.pop() for x in arr]


def sort_array(numbers):
    evens = []
    odds = []
    for a in numbers:
        if a % 2:
            odds.append(a)
            evens.append(None)
        else:
            evens.append(a)
    odds = iter(sorted(odds))
    return [next(odds) if b is None else b for b in evens]