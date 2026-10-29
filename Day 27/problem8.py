from collections import deque

def serve_customers(customers):
    queue = deque()
    for customer in customers:
        queue.append(customer)
    while queue:
        print("Serving "+queue.popleft())

customers = ["Ravi", "Priya", "Arun"]
serve_customers(customers)