item_name = input("Enter Item Name : ")
quantity = int(input("Enter Quantity : "))
price_per_item = float(input("Enter Price per Item : "))
total = quantity * price_per_item   

discountedprice = total * 0.1
totafdiscount = total - discountedprice
gst = totafdiscount * 0.18
mrp = totafdiscount + gst

print("\n--- Shopping Bill ---")
print("Item Name : ",item_name) 
print("Quantity : ",quantity)
print("Price per Item : ",price_per_item)
print("Total : ",total)
print("Total After Discount of 10% : ", totafdiscount)
print("MRP : ", mrp)
print("------------------------")