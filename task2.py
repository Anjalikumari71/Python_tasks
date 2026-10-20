product_name = input("Enter the product name: ")
quantity = input("Number of quantity: ")
product_cost = input("Product cost is: ")
print("Total cost: ", quantity * product_cost)
gst = 0.18
print("Gst: ", gst)
print("Including tax: ", quantity * product_cost * (1 + gst))