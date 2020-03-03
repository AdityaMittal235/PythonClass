# Q5. Let's plan some shopping. We want to get some fruits, veggies and dairy products:
fruits = ['Banana', 'Apple', 'Lemon', 'Orange']
veggies = ['Carrot', 'Pumpkin']
dairy = ['Milk', 'Cheese', 'Butter']

# 5.1 Check how many product from each category we want to buy
frcount=len(fruits)
vegcount=len(veggies)
dacount=len(dairy)

print("We want to buy",frcount,"fruits,", vegcount,"veggies and",dacount,"dairy products")


# 5.2 Create one shopping list called basket with all the products
basket=[fruits]+[veggies]+[dairy]

# 5.3 We forgot about cucumber - can you add it to the list of veggies?
veggies.append("Cucumber")
print("Updated Veggies: ",veggies)

# 5.4 Let's check what is in our basket now:
print(basket)
# Is cucumber in the basket? Can you fix it?
basket.append("Cucumber")
print(basket)

# We create one more list called sweets:
sweets = ['Chocolate', 'Biscuits']

# 5.5 Try to add sweets to the basket using append() and extend() methods. Do you see the difference?
basket.append(sweets)
print("Appended: ", basket)
basket.extend(sweets)
print("extended: ", basket)

