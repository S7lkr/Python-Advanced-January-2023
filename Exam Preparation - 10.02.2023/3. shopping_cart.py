def shopping_cart(*args):
    products = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    cart = {"Soup": [], "Pizza": [], "Dessert": []}
    result = []

    for data in args:
        if data == "Stop":
            break
        meal, ingredient = data
        if meal in products.keys() and len(cart[meal]) < products[meal] and ingredient not in cart[meal]:
            cart[meal].append(ingredient)

    if cart["Soup"] or cart["Pizza"] or cart["Dessert"]:
        for k, v in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0])):
            result.append(f"{k}:")
            for i in sorted(v):
                result.append(f" - {i}")
        return "\n".join(result)

    return f"No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
