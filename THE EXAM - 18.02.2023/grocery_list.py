def shop_from_grocery_list(budget, shop_list, *args):
    purchased = []
    not_purchased = []
    stop_shopping = False
    for info in args:
        prod, price = info
        if stop_shopping:
            not_purchased.append(prod)
            continue
        if float(price) > budget:
            not_purchased.append(prod)
            stop_shopping = True
            continue
        if prod in shop_list and prod not in purchased:
            purchased.append(prod)
            budget -= float(price)
        if not budget:
            break
    else:
        if not stop_shopping:
            not_purchased = set(shop_list).difference(purchased)
    if len(shop_list) == len(purchased):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    return f"You did not buy all the products. Missing products: {', '.join(not_purchased)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))