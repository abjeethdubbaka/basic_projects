# import math
# def narcissistic(value):
#     power = len(str(value))
#     sum = 0
#     for x in str(value):
#         sum = sum+math.pow(int(x),power)
#     if sum == value:
#         return True
#     else:
#         return False
# print(narcissistic(153))

def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
print(narcissistic(153))