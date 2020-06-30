#JACOB CLARK 001190089

import csv
import Model
import HashTable

def load_packages_from_CSV():
	with open('../assets/csv/packages.csv') as csvfile:
		packages = csv.reader(csvfile)
		for data_row in packages:
			new_package = Package(*data_row)
			if new_package.deliver_by == 'EOD':
				packages_hash_table.insert_kvp(new_package.package_ID, new_package)
			else:
				priority_packages_hash_table.insert_kvp(new_package.package_ID, new_package)