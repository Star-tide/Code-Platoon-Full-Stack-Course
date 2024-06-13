class CarManager:

    #Constructor/Instance Variables
    def __init__(self, all_cars=[]):
       self._all_cars = all_cars
    
    def __repr__ (self):
       return f'{CarManager.all_cars}'

    #properties
    @property
    def get_id(self):
        return self._id
    
    @property
    def get_make(self):
       return self._make
    
    @property
    def get_model(self):
       return self._model
    
    @property
    def get_year(self):
       return self._year
    
    @property
    def get_mileage(self):
       return self._milage
    
    @get_mileage.setter
    def set_mileage(self, new_odo):
       self._milage = new_odo

    @property
    def get_services(self):
       return self._services
    
    def add_a_car(self, make, model, year, mileage):
       car_object = {}
       car_object[len(CarManager.all_cars) + 1] = {
          "make" : make,
          "model" : model,
          "year" : year,
          "mileage" : mileage
       }
    def get_all_cars(self):
       return list(CarManager.all_cars)

dealership = CarManager("Kawasaki", "Ninja", 2015, 25350)
dealership.add_a_car("Kawasaki", "Ninja", 2015, 25350)
print(dealership)


def menu():
    user_choice = input(''' ----  WELCOME  ----
    1. Add a car
    2. View all cars
    3. View total number of cars
    4. See a car's details
    5. Service a car
    6. Update mileage
    7. Quit 
    \n                    
    Please Select a choice:''')

    match user_choice:
       case 1: pass
       case 2: pass
       case 3: pass
       case 4: pass
       case 5: pass
       case 6: pass
       case 7: pass
       case _: 
          return f'Please try again'
       


menu()