def shop_from_grocery_list(budget, *args, **kwargs):
    remainig_budget = budget

    for product in args:
        if product in kwargs:
            kwargs[product] -= budget
        print(remainig_budget)







print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))


