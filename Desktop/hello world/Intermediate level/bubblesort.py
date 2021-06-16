# Ascending
def bubblesort(x):
    for num in range(len(x)-1, 0, -1):
        for index in range(num):
            if x[index] > x[index+1]:
                temp = x[index]
                x[index] = x[index+1]
                x[index+1] = temp


x = [22, 15, 17, 2, 56, 32, 4]

bubblesort(x)
print(x)

# Descending Order
def bubblesort(x):
    for num in range(len(x)-1, 0, -1):
        for index in range(num):
            if x[index] < x[index+1]:
                temp = x[index]
                x[index] = x[index+1]
                x[index+1] = temp


x = [22, 15, 17, 2, 56, 32, 4]

bubblesort(x)
print(x)

