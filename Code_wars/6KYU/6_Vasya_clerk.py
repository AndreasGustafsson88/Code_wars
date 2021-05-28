def tickets(people):
    print(people)
    register = [[] for _ in range(3)]
    index25 = 0
    index50 = 0
    for n in people:
        if n == 25:
            register[0].append(n)
        elif n == 50:
            register[1].append(n)
            try:
                if register[0][index25]:
                    index25 += 1
            except IndexError:
                return "NO"
        else:
            register[2].append(n)
            try:
                if register[0][index25]:
                    pass
                if register[1][index50]:
                    index25 += 1
                    index50 += 1
            except IndexError:
                try:
                    if register[0][index25 + 2]:
                        index25 += 3
                except IndexError:
                    return "NO"
    return "YES"



print(tickets([25, 25, 25, 100]))
print(tickets([25, 25, 25, 25, 50, 100, 50]))
print(tickets([25, 25, 50]))
print(tickets([50, 100, 100]))


