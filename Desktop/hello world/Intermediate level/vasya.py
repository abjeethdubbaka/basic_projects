
# The new "Avengers" movie has just been released! There are a lot of people
# at the cinema box office standing in a huge line. Each of them has a single 100, 50 or
# 25 dollar bill. An "Avengers" ticket costs 25 dollars.
# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

def tickets(people):
    l=[0,0]
    for i in people:
        if i==25:
            l[0]+=1
        elif i==50:
            if l[0]==0:
                return "NO"
            else:
                l[0]-=1
                l[1]+=1
        else:
            if l[1]>=1:
                if l[0]==0:
                    return "NO"
                else:
                    l[0]-=1
                    l[1]-=1
            else:
                if l[0]<3:
                    return "NO"
                else:
                    l[0]-=3
    return "YES"
