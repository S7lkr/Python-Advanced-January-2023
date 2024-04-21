from collections import deque

#                                      [fuel, distance]                     number of stations
all_stations = deque([[int(s) for s in input().split(" ")] for pump in range(int(input()))])
# The above comprehension consists of a for-loop, nested in another for-loop

all_stations_copy = all_stations.copy()     # a copy of the original DECK is mandatory, because when we use
idx = 0                                     # a while-loop it should stop (all the elements must end) at some point
fuel_in_tank = 0

while all_stations_copy:
    fuel, distance = all_stations_copy.popleft()
    fuel_in_tank += fuel
    if fuel_in_tank - distance < 0:     # fuel not enough to go to next pump
        all_stations.rotate(-1)     # move 1st element at the end: stations.append(stations.popleft())
        all_stations_copy = all_stations.copy()
        fuel_in_tank = 0    # after calculating route, we will not add fuel
        idx += 1    # here fuel won't be enough, so we'll "try" next station
    else:
        fuel_in_tank -= distance

print(idx)