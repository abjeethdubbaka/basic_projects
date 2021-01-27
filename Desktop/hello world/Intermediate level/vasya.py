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
