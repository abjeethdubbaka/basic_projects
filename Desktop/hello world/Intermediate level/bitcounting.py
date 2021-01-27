# def count_bits(n):
#     count = 0
#     while n>0:
#         if (n&1) == 1:
#             count = count+1
#         n>>1
#     return count

def count_bits(n):
    return bin(n).count('1')