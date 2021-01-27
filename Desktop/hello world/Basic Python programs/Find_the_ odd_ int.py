# def oddoccur(listn):
#     print('Find the only integer which occurs an odd number of times in a given array. \n')
#     for n in range(len(listn)):
#         k = listn[n]
#         if listn.count(k) % 2 == 1:
#             print(listn[n], 'occurs', listn.count(k), 'times in the array:')
#             print(listn)
#             break
#
#
# ilist = [1, 2, 3, 4, 5, 6, 4, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 4, 4]
# oddoccur(list)

def find_it(seq):
    for n in range(len(seq)):
        k = seq[n]
        if seq.count(k) % 2 == 1:
            return seq[n]
