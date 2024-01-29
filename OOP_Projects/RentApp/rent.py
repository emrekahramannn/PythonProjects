# import libraries
import datetime


# Parent Class
class VehicleRent:

    def __init__(self, stock):
        self.stock = stock       # total vehicle in stock
        self.now = 0             # to calculate bill (amount of money)
    
    def displayStock(self):
        """display stock"""
        print(f"{self.stock} vehicle available to rent")
        return self.stock

    def rentHourly(self, n):
        """rent hourly"""
        if n <= 0:
            print("Number should be positive.")
            return None
        elif n > self.stock:
            print(f"Sorry. {self.stock} vehicle available to rent.")
        else:
            # time which vehicle rented
            self.now = datetime.datetime.now()  # take the local time when customer rent the car 
            print(f"Rented {n} vehicle for hourly at {self.now.hour}.")

            self.stock = self.stock - n

            return self.now
        


    def rentDaily(self, n):
        """rent daily"""
        if n <= 0:
            print("Number should be positive.")
            return None
        elif n > self.stock:
            print(f"Sorry. {self.stock} vehicle available to rent.")
        else:
            self.now = datetime.datetime.now()  # take the local time when customer rent the car 
            print(f"Rented {n} vehicle for daily at {self.now.hour}.")

            self.stock = self.stock - n

            return self.now



    def returnVehicle(self, request, brand):
        """return a bill"""
        car_h_price = 10
        car_d_price = car_h_price * 8 / 10 * 24

        bike_h_price = 5
        bike_d_price = bike_h_price * 7 / 10 * 24

        rentalTime, rentalBasis, numberOfVehicle = request 
        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numberOfVehicle:

                self.stock += numberOfVehicle       # update stock

                now = datetime.datetime.now()       # return time

                rentalPeriod = now - rentalTime     # hours rented

                if rentalBasis == 1:
                    # hourly rented
                    bill = rentalPeriod.seconds / 3600 * car_h_price * numberOfVehicle

                elif rentalBasis == 2:
                    # daily rented
                    bill = rentalPeriod.seconds / (3600 * 24) * car_d_price * numberOfVehicle

                if (2 <= numberOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill * 0.8

                print("Thank you for returning your car.")   
                print(f"Price: ${bill}.") 
                return bill 


        elif brand == "bike":
            if rentalTime and rentalBasis and numberOfVehicle:

                self.stock += numberOfVehicle       # update stock

                now = datetime.datetime.now()       # return time

                rentalPeriod = now - rentalTime     # hours rented

                if rentalBasis == 1:
                    # hourly rented
                    bill = rentalPeriod.seconds / 3600 *bike_h_price * numberOfVehicle

                elif rentalBasis == 2:
                    # daily rented
                    bill = rentalPeriod.seconds / (3600 * 24) * bike_d_price * numberOfVehicle

                if (4 <= numberOfVehicle):
                    print("You have extra 15% discount")
                    bill = bill * 0.85

                print("Thank you for returning your bike.")   
                print(f"Price: ${bill}.") 
                return bill   

        else:
            print("You have not rent any vehicle")  
            return None      



# Child (Sub) Class 
class CarRent(VehicleRent):

    global discount_rate
    discount_rate = 15

    def __init__(self, stock):
        super().__init__(stock)
        

    def discount(self, b):
        """discount"""
        bill = b - (b * discount_rate) / 100
        return bill


# Child (Sub) Class 
class BikeRent(VehicleRent):

    def __init__(self, stock):
        super().__init__(stock)






class Customer:

    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0
        
        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0


    def requestVehicle(self, brand):
        """
        take a request bike or car from customer"""
        if brand == "bike":
            bikes = input("How many bikes would you like to rent: ")
            try:
                bikes = int(bikes)
            except ValueError:
                print("\nInvalid Input")
                return -1
            
            if bikes < 1:
                print("Number of Bikes should be greater than zero.")
                return -1
            else:
                self.bikes = bikes
            
            return self.bikes
        
        elif brand == "car":
            cars = input("How many cars would you like to rent: ")
            try:
                cars = int(cars)
            except ValueError:
                print("\nInvalid Input")
                return -1
            
            if cars < 1:
                print("Number of Cars should be greater than zero.")
                return -1
            else:
                self.cars = cars
            
            return self.cars
        
        else:
            print("Request vehicle error.")
        




    def returnVehicle(self, brand):
        """return bikes or cars"""

        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0

        
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0,0,0


        else:
            print("Return vehicle error.")