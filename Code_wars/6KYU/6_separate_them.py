def namelist(names):
    res = ""
    for i, name in enumerate(names, 1):
        if len(names) - i > 1:
            for k in name.keys():
                res += name[k] + ", "
        if len(names) - i == 1:
            for k in name.keys():
                res += name[k] + " & "
        if len(names) - i == 0:
            for k in name.keys():
                res += name[k]

    return res


print(namelist([
    {'name': 'Bart'},
    {'name': 'Lisa'},
    {'name': 'Maggie'},
    {'name': 'Homer'},
    {'name': 'Marge'}]))

print(namelist([
    {'name': 'Bart'},
    {'name': 'Lisa'},
    {'name': 'Maggie'}]))

print(namelist([
    {'name': 'Bart'}]))
print(namelist([
    {'name': 'Bart'},
    {'name': 'Lisa'}]))
