from collections import deque

food_quantity = int(input())

order_quantity = deque([int(x) for x in input().split()])
copy_of_order_quantity = order_quantity.copy()
print(max(order_quantity))

for order in copy_of_order_quantity:
    order_size = order
    food_quantity -= order_size
    if order_quantity and food_quantity >= 0:
        order_quantity.popleft()
    else:
        print(f"Orders left: {' '.join([str(x) for x in order_quantity])}")
        raise SystemExit
print("Orders complete")
