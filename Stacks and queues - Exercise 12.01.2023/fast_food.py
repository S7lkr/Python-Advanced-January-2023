from collections import deque

food_quantity = int(input())
orders = deque([int(i) for i in input().split(" ")])
print(max(orders))

for order in orders.copy():
    if food_quantity - order >= 0:
        food_quantity -= orders.popleft()
    else:
        print(f"Orders left: {' '.join([str(order) for order in orders])}")
        break
else:
    print("Orders complete")


# from collections import deque
#
# food_quantity = int(input())
# orders = deque([int(i) for i in input().split(" ")])
# print(max(orders))
#
# while food_quantity and orders:
#     if orders[0] <= food_quantity:
#         food_quantity -= orders.popleft()
#     else:
#         break
#
# if not orders:
#     print("Orders complete")
# else:
#     print(f"Orders left: {' '.join([str(order) for order in orders])}")