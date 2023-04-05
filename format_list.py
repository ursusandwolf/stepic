def format_name_list(ditionaries):
    names = []
    for d in ditionaries:
        names.append(d['name'])

    if len(names) == 1:
        return names[0]
    if len(names) > 1:
        a,b,c = "", names[-2], names[-1]
        for i in range(len(names)-2):
            a +=f"{names[i]}, "
        return f"{a}{b} and {c}"
    return ""

dictionaries = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
print(format_name_list(dictionaries))
