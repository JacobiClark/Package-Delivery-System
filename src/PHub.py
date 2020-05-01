import csv
from Package import Package
from HashTable import HashTable
import collections
# Hub class
class PHub:
    def start(self):
        packages_hash_table = HashTable(50)

        with open('../assets/csv/packages.csv') as csvfile:
            packages = csv.reader(csvfile)
            for data_row in packages:
                new_package = Package(*data_row)
                packages_hash_table.insert_kvp(new_package.get_package_id, new_package)

    
phub = PHub()
phub.start()


