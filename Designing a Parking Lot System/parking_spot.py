from vehicle_type import VehicleType
from vehicle import Vehicle

class ParkingSpot:
    def __init__(self, spot_number: int, vehicle_type: VehicleType):
        self.spot_number = spot_number
        self.vehicle_type = vehicle_type
        self.parked_vehicle = None
    
    def is_available(self) -> bool:
        return self.parked_vehicle is None
    
    def park_vehicle(self,vehicle:Vehicle) -> None:
        if self.is_available() and vehicle.get_type() == self.vehicle_type: self.parked_vehicle = vehicle

    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None
    
    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type
    
    def get_parked_vehicle(self):
        return self.parked_vehicle
    
    def get_spot_number(self)-> int:
        return self.spot_number