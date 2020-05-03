import datetime

class Truck:
    max_packages = 16
    avg_speed_MPH = 18
    start_time = datetime.time(8, 00, 00)

    def __init__(self, truck_number, start_location):
        self.max_packages = max_packages
        self.avg_speed_MPH = avg_speed_MPH
        self.start_time = start_time
        self.truck_number = truck_number
        self.start_location = start_location
        self.distance_driven = 0
        self.packages_onboard = []

    def load_package(self, package, deliver_by)
        if len(self.packages_onboard) < self.max_packages:
            self.packages_onboard.append(package)


Baja = Truck(3,a)
Baja.add_package('blah')