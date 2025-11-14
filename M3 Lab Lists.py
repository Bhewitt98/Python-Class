#Vehicle superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#Automobile class        
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
#Input section
def main():
    print("Please enter vehicle type (car, boat, motorcycle, plane, etc.): ")
    vehicle_type = input().lower()
    
    if vehicle_type == "car":
        print("Please enter the details of your vehicle:\n")
        
        year = input("Enter Year: ")
        make = input("Enter Make: ")
        model = input("Enter Model: ")        
        
        while True:
            doors = input("Number of doors (2 or 4): ")
            if doors in ("2", "4"):
                break
            print("Please enter 2 or 4: ")
            
        while True:
            roof = input("Enter Roof style (solid or sun roof): ").lower()
            if roof in ("solid", "sun roof"):
                break
            print("Please enter 'solid' or 'sun roof': ")
        
        car = Automobile(year, make, model, doors, roof)
            
        print("\nYour vehicle information:\n")
        print(f"Vehicle Type: {car.vehicle_type}")
        print(f"Year: {car.year}")
        print(f"Make: {car.make}")
        print(f"Model: {car.model}")
        print(f"Doors: {car.doors}")
        print(f"Roof: {car.roof}")
    
    else:
        print("Unfortunately, that vehicle type is not supported.")
    
if __name__ == "__main__":
    main()

    
        

           