   
inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]
# print(inventory)



# 1.calculate the TotalRevenue


total_revenue = 0
for name,cat,unitprice,unitsold,unitleft in inventory:
    revenue = unitprice * unitsold
    total_revenue += revenue
print(total_revenue) 
print("---------------------------")

# 2. List Low stock item if stock is less than 5
for item in inventory:
    name, category, unit_price, units_sold, units_left = item
    if units_left < 5:
        print(item)
print("---------------------------")

      
# 3.calculte the categorywise Revenue


total_revenue = 0
for item in inventory:
    name, category, unit_price, units_sold, units_left = item
    revenue = unit_price * units_sold 
    print(f"{name} revenue: {revenue:.2f}")
    total_revenue += revenue  # <- Don't comment this out

# print(f"\nRevenue from all products: {total_revenue:.2f}")


    
    
    
 
  

    