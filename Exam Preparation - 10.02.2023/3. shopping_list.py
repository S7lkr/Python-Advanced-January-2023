def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    basket = 5
    result = []
    for product, info in kwargs.items():
        price, qnt = info
        total_price = price * qnt
        if total_price <= budget:
            result.append(f"You bought {product} for {total_price:.2f} leva.")
            budget -= total_price
            basket -= 1
        if not budget or not basket:
            break
    return "\n".join(result)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))