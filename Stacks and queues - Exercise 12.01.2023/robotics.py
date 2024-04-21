from collections import deque
from datetime import datetime, timedelta

# robots -> dict.  {rob_name:  [time_needed_for_task,   time_on_curr_task]}
robots = {robot.split("-")[0]: [int(robot.split("-")[1]), 0] for robot in input().split(";")}

factory_time = datetime.strptime(input(), "%H:%M:%S")  # this method sets a starting time
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    factory_time += timedelta(0, 1)    # 0 is days, 1 is seconds. We will add 1 sec. every iteration
    product = products.popleft()
# Now we need to decrease "time_on_task" with 1 sec. (on every loop)
#             name:  [time_needed, time_on_task - 1]
    robots = {rob[0]: [rob[1][0], rob[1][1] - 1] if rob[1][1] != 0 else rob[1] for rob in robots.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))  # list with free robots
    if not free_robots:     # if there are NO free robots:
        products.append(product)
        continue
    robots[free_robots[0][0]][1] = free_robots[0][1][0]
    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")