# Create a Parcel class that contains the following attributes: width, length, height. The class also contains a field to count the number of parcels. Create an array of objects such as
# "Parcel".
# Create several objects of the "Parcel" class and write them in an array. Find the smallest parcel. Check the number of existing parcels.
# If this value exceeds any limit value - display a message.
from functools import reduce

class Parcel:

    stock = []
    stock_value = []
    parcel_amount = 0

    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        Parcel.parcel_amount += 1
        if Parcel.parcel_amount > 5:
            print("You exceed maximum parcel amount!!!")

    def parcel_stock(self):
        Parcel.stock.append([self.width,self.length, self.height])

    def parcel_size(self):
        for i in Parcel.stock:
            Parcel.stock_value.append(reduce(lambda a, b: a * b, i))

    def smallest_size(self):
        print("Smallest parcel in stock is:",min(x for x in Parcel.stock_value),"m3")



p1 = Parcel(5,6,1)
p2 = Parcel(2,4,3)
p3 = Parcel(8,4,1)
p4 = Parcel(1,4,1)
p5 = Parcel(1,4,8)
p6 = Parcel(2,2,4)
p1.parcel_stock()
p2.parcel_stock()
p3.parcel_stock()
p4.parcel_stock()
p5.parcel_stock()
p6.parcel_stock()
print("Total parcels in stock:",Parcel.parcel_amount)
print("Parcels sizes in stock:",Parcel.stock)
p1.parcel_size()
print("Volume of each parcel in stock:",Parcel.stock_value)
p1.smallest_size()