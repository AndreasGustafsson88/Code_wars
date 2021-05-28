def wave(people):
    result = [people for _ in people]
    fin = []
    for i, wave in enumerate(result):
        if wave[i].isalpha():
            result[i] = wave[0:i] + wave[i].upper() + wave[i + 1:]

    for i, n in enumerate(people):
        if n != " ":
            fin.append(result[i])
    return fin


print(wave("  gap  "))