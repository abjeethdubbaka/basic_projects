def solution(s):
    list_1 = []
    if len(s) % 2 != 0:
        s += "_"
    for i in range(0,len(s), 2):
        list_1.append(s[i:i+2])
    return list_1
print(sorted("abjeeth"))
