#: Bubble sort
def bubblesort(array):
    issorted =  False
    counter = 0
    while not  issorted:
        issorted = True
        for i in range(len(array)-1 - counter):
            if array[i]> array[i+1]:
                swap(i, i+1, array)
                issorted = False
        counter +=1
    return array

def swap(i,j,array):
    array[i], array[j] = array[j],array[i]
