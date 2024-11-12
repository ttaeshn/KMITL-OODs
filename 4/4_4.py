class Queue:
    def __init__(self, lst=None):
        self.items = [] if lst is None else lst

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[0] if not self.is_empty() else None

def process_customer(cashier, waiting, customer, time_count, max_time, max_customer):
    start_time = int(waiting.dequeue())
    duration = int(waiting.dequeue())
    customer += 1
    service_time = max(time_count, start_time) + duration
    cashier.enqueue(service_time)
    cashier.enqueue(customer)
    waiting_time = time_count - start_time
    if waiting_time > max_time:
        max_time = waiting_time
        max_customer = customer
    return customer, max_time, max_customer

def serve_customers(cashier, waiting, time_count, customer, max_time, max_customer):
    if not cashier.is_empty() and time_count >= int(cashier.front()):
        cashier.dequeue()
        served_customer = cashier.dequeue()
        print(f"Time {time_count} customer {served_customer} gets coffee")
        if cashier.size() < 2 and not waiting.is_empty():
            customer, max_time, max_customer = process_customer(cashier, waiting, customer, time_count, max_time, max_customer)
    return customer, max_time, max_customer

print(" ***Cafe***")
log = input("Log : ").split("/")
waiting, cashier1, cashier2 = Queue(), Queue(), Queue()

for entry in log:
    start, duration = entry.split(",")
    waiting.enqueue(start)
    waiting.enqueue(duration)

customer, time_count, max_time, max_customer = 0, 0, 0, 0
while not (waiting.is_empty() and cashier1.is_empty() and cashier2.is_empty()):
    while (cashier1.is_empty() or cashier2.is_empty()) and not waiting.is_empty():
        if cashier1.size() < 2:
            customer, max_time, max_customer = process_customer(cashier1, waiting, customer, time_count, max_time, max_customer)
        if cashier2.size() < 2 and not waiting.is_empty():
            customer, max_time, max_customer = process_customer(cashier2, waiting, customer, time_count, max_time, max_customer)

    time_count += 1

    if cashier1.front() == cashier2.front():
        if int(cashier1.items[1]) < int(cashier2.items[1]):
            customer, max_time, max_customer = serve_customers(cashier1, waiting, time_count, customer, max_time, max_customer)
            customer, max_time, max_customer = serve_customers(cashier2, waiting, time_count, customer, max_time, max_customer)
        else:
            customer, max_time, max_customer = serve_customers(cashier2, waiting, time_count, customer, max_time, max_customer)
            customer, max_time, max_customer = serve_customers(cashier1, waiting, time_count, customer, max_time, max_customer)
    else:
        customer, max_time, max_customer = serve_customers(cashier1, waiting, time_count, customer, max_time, max_customer)
        customer, max_time, max_customer = serve_customers(cashier2, waiting, time_count, customer, max_time, max_customer)

if max_time != 0:
    print(f"The customer who waited the longest is : {max_customer}\nThe customer waited for {max_time} minutes")
else:
    print("No waiting")