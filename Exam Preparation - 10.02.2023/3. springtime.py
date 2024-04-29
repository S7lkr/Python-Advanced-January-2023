def start_spring(**kwargs):
    collections = {}
    result = []
    for obj, kind in sorted(kwargs.items()):
        if kind not in collections.keys():
            collections[kind] = []
        collections[kind].append(obj)
    for key, value in sorted(collections.items(), key=lambda x: (-len(x[1]), x[0], x[1])):
        result.append(f"{key}:")
        for v in sorted(value):
            result.append(f"-{v}")
    return "\n".join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))