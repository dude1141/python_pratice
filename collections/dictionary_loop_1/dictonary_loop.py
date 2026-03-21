# Assume that you are a developer at zomoato. You are
#building the add to cart functionality. Ask the user
# name of the product and price.
# Here user can add 1 to 5 items
# Ask the user  if he want to coninue adding more
# if yes then allow him to add.
# At the end display the product and price corresponding
# it.
productcart={}

for i in range(0,5):
    product =input("product details: ")
    price = int(input("price details: "))

    productcart[product] = price
    
    while True:
        choice = input("do you want to continue")

        if choice == "No":
            break
        elif choice == "Yes":
            break
        else:
            print("wrong choice enter again")
            
    if choice =="No":
        break
for i in productcart:
    print(i)
    print(productcart[i])






    