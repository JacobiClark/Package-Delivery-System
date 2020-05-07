import datetime

class Truck:
   
    def __init__(self, truck_number, start_location):
        self.max_packages = 16
        self.avg_speed_MPH = 18
        self.start_time = datetime.time(8, 00, 00)
        self.truck_number = truck_number
        self.start_location = start_location
        self.distance_driven = 0
        self.delivery_list = []

    def load_package(self, package, deliver_by):
        if len(self.delivery_list) < self.max_packages:
            self.delivery_list.append(package)

    #def deliver_packages(self):
    #    while len(self.delivery_list) > 0:

    def has_room(self):
        if len(self.delivery_list) < self.max_packages:
            return true
        else:
            return false