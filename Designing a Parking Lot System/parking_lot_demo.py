from parking_lot import ParkingLot
from level import Level
from car import Car
from truck import Truck
from motorcycle import Motorcycle

class ParkingLotDemo:
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1,10))
        parking_lot.add_level(Level(2,12))

        car = Car("ABC123")
        truck = Truck("XYZ789")
        motorcycle = Motorcycle("M1234")


        # Park Vehicle

        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(motorcycle)


        #Display Availability 

        parking_lot.display_availability()


        #unpark  Vehicle
        parking_lot.unpark_vehicle(motorcycle)

        #Display updated Availability

        parking_lot.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.run()