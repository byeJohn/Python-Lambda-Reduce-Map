new_list = [80,90,77]

final = 85

lowest = reduce(lambda a,b: a if (a<b) else b, new_list)

print(lowest)

map_list = map(lambda a:final if (a == lowest and a < final) else a, new_list)

print(list(map_list))
