# Create a mobile phone class
class MobilePhone:
    # constructor
    def __init__(self,Brand,Model,StorageCapacity,Price):
        # set the object's brand to the brand typed
        self.Brand = Brand
        # set the object's model to the model typed
        self.Model = Model
        # set the object's storage capacity to the storage capacity typed
        self.StorageCapacity = StorageCapacity
        # set the object's price to the price typed
        self.Price = Price
    
    #methods
    # method to print details of the phone
    def DisplayPhoneDetails(self):
        # display phone details
        print(f"Brand: {self.Brand}\nModel: {self.Model}\nStorage Capacity: {self.StorageCapacity}\nPrice: ${self.Price:.2f}\n")
            
# create the first phone object
phoneObj1 = MobilePhone("Samsung","Vers 1.0","5KB",50)
# create the second phone object
phoneObj2 = MobilePhone("Samsung but BETTER","Vers 1.001","5.3KB",900)

# display the details of the first phone object
phoneObj1.DisplayPhoneDetails()
# display the details of the second phone object
phoneObj2.DisplayPhoneDetails()