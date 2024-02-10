class Bike:

    def __init__(self,description, condition, sale_price, cost=0):
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost
        self.sold = False


    def update_sale_price(self,new_sale_price):
        if new_sale_price<0:
            raise ValueError("saleprice cannot be negative")
        self.sale_price=new_sale_price


    def sell(self):
        """sell doctstring returns profit from sale"""
        self.sold=True
        profit=self.sale_price-self.cost
        return  profit

    def service(self):
        pass

#__init is initialiazer

#everything in python is object
#ininstance(print , object)
#pass or ...

#Bike() is instance
    #
if __name__ == "__main__":
    #allows you to define code that should only run when the script is executed directly,
    # and not when it's imported as a module.

    my_bike= Bike("orange","okay",sale_price=300,cost=50)
    # my_bike.sell()

    print(my_bike.sell())
    #__init__ gets called when ever you instantiate a new bike
    # my_bike2= Bike()
    # print(my_bike2)
    print("----------->>"+__name__)
    my_bike.sell()
    #my_bike.sell() is Bike.sell(my_bike) background

    #init gets called everytime you instantiate a new bike
