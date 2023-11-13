from collections import deque

customer_name = input()
customers = deque()

while customer_name != "End":

    if customer_name != "Paid":
        customers.append(customer_name)

    if customer_name == "Paid":
        for _ in range(len(customers)):
            print(customers.popleft())

    customer_name = input()
print(f"{len(customers)} people remaining.")
