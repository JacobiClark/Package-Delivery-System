import datetime

class Package:
    def __init__(self, package_ID, address, city, state, zipcode, deliver_by, weight_in_kilograms, status):
        self.package_ID = int(package_ID)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipcode
        if 'EOD' in deliver_by:
            self.deliver_by = "EOD"
        else: self.deliver_by = datetime.datetime.strptime(deliver_by, '%H:%M').time()
        self.weight_in_kilograms = weight_in_kilograms
        self.deliver_by = deliver_by
        self.status = status

    def get_package_id(self):
        return int(self.package_ID)

