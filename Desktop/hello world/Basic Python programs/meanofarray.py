# def get_average(marks):
#     for avg in marks:
#         x = len(marks)
#         y = sum(marks)
#         z = x//y
#         return z
# marks = [26,54,74,76]
# k = get_average(marks)
# print(k)
import math
def get_average(marks):
    total = 0
    mean = len(marks)
    for i in marks:
        total += i
    return math.floor(total/mean)
marks = [26,54,74,76]
k = get_average(marks)
print(k)
