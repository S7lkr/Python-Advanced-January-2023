vehicles = [input().split(", ") for _ in range(int(input()))]
cars = set()

for car in vehicles:
    if car[0] == "IN":
        cars.add(car[1])
    else:
        cars.remove(car[1])
if cars:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")