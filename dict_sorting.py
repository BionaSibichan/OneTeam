stock = {
    "Laptop": 23,
    "Mouse": 12,
    "Monitor": 3,
    "Keyboard": 15,
    "Printer": 5
}

print("By name:", sorted(stock.items()))
print("By stock ascending:", sorted(stock.items(), key=lambda x: x[1]))
print("By stock descending:", sorted(stock.items(), key=lambda x: x[1], reverse=True))
print("Stock < 10:", [k for k, v in stock.items() if v < 10])