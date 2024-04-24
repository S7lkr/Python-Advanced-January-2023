def fill_the_box(h, l, w, *cubes_data):
    cube_size = h * l * w
    capacity = cube_size
    for cubes in cubes_data:
        if cubes == "Finish":
            if capacity > 0:
                return f"There is free space in the box. You could put {capacity} more cubes."
            else:
                return f"No more free space! You have {abs(capacity)} more cubes."
        capacity -= cubes


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))