from collections import deque

pizza_orders = deque(list(map(int, input().split(", "))))
employees = deque(list(map(int, input().split(", "))))
pizzas_made = 0

while pizza_orders and employees:
    pizzas = pizza_orders.popleft()
    if pizzas <= 0 or pizzas > 10:
        continue
    employee = employees.pop()
    if pizzas <= employee:
        pizzas_made += pizzas
    else:
        pizzas_made += employee
        pizza_orders.appendleft(pizzas - employee)

else:
    if not pizza_orders:
        print("All orders are successfully completed!")
        print(f"Total pizzas made: {pizzas_made}")
        print(f"Employees: {', '.join([str(emp) for emp in employees])}")
    else:
        print("Not all orders are completed.")
        print(f"Orders left: {', '.join([str(order) for order in pizza_orders])}")