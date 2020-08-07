#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]


# Parent-------------------------------------------------------------
class Vehicle:
    def __init__(self):
        pass


# Gen 1 Child-------------------------------------------------------
class GroundVehicle(Vehicle):
    def __init__(self):
        pass


# Gen 2 Children ---------------------------------------------------
class Car(GroundVehicle):
    def __init__(self):
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        pass


# Gen 1 Child-------------------------------------------------------
class FlightVehicle(Vehicle):
    def __init__(self):
        pass

# Gen 2 Children-----------------------------------------------------
class Airplane(FlightVehicle):
    def __init__(self):
        pass

class Starship(FlightVehicle):
    def __init__(self):
        pass


