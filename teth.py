import json
with open('lalaland.txt') as file, open('dump.json', 'w') as json_file:
    items = []
    for line in file:
        if not line.strip():
            continue
        d = {}
        data = line.split('|')
        for val in data:
            key, sep, value = val.partition(':')
            d[key.strip()] = value.strip()
        items.append(d)
    json.dump(items, json_file)

print(items)